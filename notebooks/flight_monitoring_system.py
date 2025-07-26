import os
import json
import time
from datetime import datetime
from byteplussdkarkruntime import Ark

class FlightMonitoringSystem:
    def __init__(self):
        """Initialize the flight monitoring system"""
        self.client = Ark(
            base_url="https://ark.ap-southeast.bytepluses.com/api/v3",
            api_key=os.environ.get("ARK_API_KEY"),
        )
        self.flight_data = {}
        self.alerts = []
        
    def analyze_flight_image(self, image_url, flight_info=None):
        """
        Analyze flight-related images and extract structured information
        
        Args:
            image_url (str): URL of the flight image
            flight_info (dict): Optional flight information for context
            
        Returns:
            dict: Structured flight analysis results
        """
        try:
            # Prepare the prompt for flight monitoring
            prompt = self._create_flight_analysis_prompt(flight_info)
            
            response = self.client.chat.completions.create(
                model="ep-20250725202540-7skq7",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {"url": image_url}
                            },
                            {"type": "text", "text": prompt}
                        ]
                    }
                ]
            )
            
            # Parse and structure the response
            result = self._parse_flight_response(response.choices[0].message.content, flight_info)
            return result
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def _create_flight_analysis_prompt(self, flight_info=None):
        """Create a structured prompt for flight analysis"""
        base_prompt = """
        Analyze this flight-related image and provide a structured response in JSON format. 
        Focus on the following aspects:
        
        1. **Flight Status**: Identify if this is a takeoff, landing, cruising, or ground operation
        2. **Aircraft Information**: 
           - Aircraft type (if visible)
           - Registration number (if visible)
           - Airline/operator (if visible)
        3. **Environmental Conditions**:
           - Weather conditions
           - Visibility
           - Time of day
        4. **Safety Assessment**:
           - Any visible safety concerns
           - Operational status
        5. **Location Context**:
           - Airport/runway identification (if possible)
           - Geographic features
        6. **Operational Details**:
           - Flight phase
           - Ground operations (if applicable)
        
        Please respond with a JSON object containing these fields:
        {
            "flight_status": "string",
            "aircraft_info": {
                "type": "string",
                "registration": "string", 
                "operator": "string"
            },
            "environment": {
                "weather": "string",
                "visibility": "string",
                "time_of_day": "string"
            },
            "safety": {
                "concerns": "string",
                "operational_status": "string"
            },
            "location": {
                "airport": "string",
                "runway": "string",
                "geographic_features": "string"
            },
            "operations": {
                "flight_phase": "string",
                "ground_operations": "string"
            },
            "confidence_score": "float (0-1)",
            "analysis_timestamp": "ISO timestamp"
        }
        """
        
        if flight_info:
            context = f"\n\nAdditional Flight Context: {json.dumps(flight_info, indent=2)}"
            base_prompt += context
            
        return base_prompt
    
    def _parse_flight_response(self, response_text, flight_info=None):
        """Parse the AI response and structure it for flight monitoring"""
        try:
            # Try to extract JSON from the response
            if "{" in response_text and "}" in response_text:
                start = response_text.find("{")
                end = response_text.rfind("}") + 1
                json_str = response_text[start:end]
                parsed_data = json.loads(json_str)
            else:
                # If no JSON found, create a structured response from text
                parsed_data = self._extract_info_from_text(response_text)
            
            # Add metadata
            parsed_data["raw_response"] = response_text
            parsed_data["flight_info"] = flight_info
            parsed_data["processed_timestamp"] = datetime.now().isoformat()
            
            return parsed_data
            
        except json.JSONDecodeError:
            # Fallback to text parsing
            return {
                "status": "parsing_error",
                "raw_response": response_text,
                "extracted_info": self._extract_info_from_text(response_text),
                "flight_info": flight_info,
                "processed_timestamp": datetime.now().isoformat()
            }
    
    def _extract_info_from_text(self, text):
        """Extract flight information from unstructured text"""
        # Simple keyword-based extraction
        info = {
            "flight_status": "unknown",
            "aircraft_info": {"type": "unknown", "registration": "unknown", "operator": "unknown"},
            "environment": {"weather": "unknown", "visibility": "unknown", "time_of_day": "unknown"},
            "safety": {"concerns": "none", "operational_status": "unknown"},
            "location": {"airport": "unknown", "runway": "unknown", "geographic_features": "unknown"},
            "operations": {"flight_phase": "unknown", "ground_operations": "unknown"},
            "confidence_score": 0.5
        }
        
        text_lower = text.lower()
        
        # Flight status detection
        if any(word in text_lower for word in ["takeoff", "take off", "departure"]):
            info["flight_status"] = "takeoff"
        elif any(word in text_lower for word in ["landing", "approach", "arrival"]):
            info["flight_status"] = "landing"
        elif any(word in text_lower for word in ["cruising", "flight", "airborne"]):
            info["flight_status"] = "cruising"
        elif any(word in text_lower for word in ["ground", "parked", "gate"]):
            info["flight_status"] = "ground_operation"
        
        # Weather detection
        if any(word in text_lower for word in ["clear", "sunny", "good"]):
            info["environment"]["weather"] = "clear"
        elif any(word in text_lower for word in ["cloudy", "overcast"]):
            info["environment"]["weather"] = "cloudy"
        elif any(word in text_lower for word in ["rain", "storm", "bad"]):
            info["environment"]["weather"] = "poor"
        
        return info
    
    def monitor_flight_sequence(self, image_urls, flight_info=None):
        """
        Monitor a sequence of flight images for continuous monitoring
        
        Args:
            image_urls (list): List of image URLs for sequential analysis
            flight_info (dict): Flight information for context
            
        Returns:
            dict: Sequential analysis results
        """
        results = []
        
        for i, image_url in enumerate(image_urls):
            print(f"Analyzing image {i+1}/{len(image_urls)}...")
            
            result = self.analyze_flight_image(image_url, flight_info)
            result["sequence_number"] = i + 1
            result["image_url"] = image_url
            
            results.append(result)
            
            # Add delay between requests to avoid rate limiting
            if i < len(image_urls) - 1:
                time.sleep(1)
        
        # Analyze the sequence for patterns and alerts
        sequence_analysis = self._analyze_sequence(results)
        
        return {
            "individual_analyses": results,
            "sequence_analysis": sequence_analysis,
            "monitoring_summary": self._generate_monitoring_summary(results)
        }
    
    def _analyze_sequence(self, results):
        """Analyze a sequence of flight images for patterns"""
        analysis = {
            "status_changes": [],
            "safety_trends": [],
            "environmental_changes": [],
            "anomalies": []
        }
        
        for i in range(1, len(results)):
            prev = results[i-1]
            curr = results[i]
            
            # Check for status changes
            if prev.get("flight_status") != curr.get("flight_status"):
                analysis["status_changes"].append({
                    "from": prev.get("flight_status"),
                    "to": curr.get("flight_status"),
                    "sequence_position": i
                })
            
            # Check for safety concerns
            if "concern" in curr.get("safety", {}).get("concerns", "").lower():
                analysis["safety_trends"].append({
                    "concern": curr["safety"]["concerns"],
                    "sequence_position": i
                })
        
        return analysis
    
    def _generate_monitoring_summary(self, results):
        """Generate a summary of the monitoring session"""
        if not results:
            return {"status": "no_data"}
        
        summary = {
            "total_images_analyzed": len(results),
            "flight_status_distribution": {},
            "safety_concerns_count": 0,
            "average_confidence": 0,
            "recommendations": []
        }
        
        # Count statuses
        for result in results:
            status = result.get("flight_status", "unknown")
            summary["flight_status_distribution"][status] = summary["flight_status_distribution"].get(status, 0) + 1
            
            # Count safety concerns
            if "concern" in result.get("safety", {}).get("concerns", "").lower():
                summary["safety_concerns_count"] += 1
        
        # Calculate average confidence
        confidences = [r.get("confidence_score", 0.5) for r in results]
        summary["average_confidence"] = sum(confidences) / len(confidences)
        
        # Generate recommendations
        if summary["safety_concerns_count"] > 0:
            summary["recommendations"].append("Safety concerns detected - review required")
        
        if summary["average_confidence"] < 0.7:
            summary["recommendations"].append("Low confidence in analysis - manual review recommended")
        
        return summary
    
    def export_results(self, results, filename=None):
        """Export monitoring results to JSON file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"flight_monitoring_results_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"Results exported to {filename}")
        return filename

# Example usage
def main():
    """Example usage of the Flight Monitoring System"""
    system = FlightMonitoringSystem()
    
    # Example flight information
    flight_info = {
        "flight_number": "AC123",
        "aircraft_type": "Boeing 737",
        "origin": "Toronto",
        "destination": "Vancouver",
        "scheduled_departure": "2025-07-25T10:00:00Z"
    }
    
    # Example image URL (replace with actual flight images)
    test_image_url = "https://ark-doc.tos-ap-southeast-1.bytepluses.com/see_i2v.jpeg"
    
    print("=== Flight Monitoring System Test ===")
    
    # Single image analysis
    print("\n1. Analyzing single flight image...")
    result = system.analyze_flight_image(test_image_url, flight_info)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # Export results
    system.export_results(result, "single_flight_analysis.json")
    
    print("\n=== Analysis Complete ===")

if __name__ == "__main__":
    main() 