#!/usr/bin/env python3
"""
Simple test script for the Flight Monitoring System
"""

import os
import json
from flight_monitoring_system import FlightMonitoringSystem

def test_basic_functionality():
    """Test basic functionality of the flight monitoring system"""
    
    # Check if API key is available
    if not os.environ.get("ARK_API_KEY"):
        print("❌ Error: ARK_API_KEY environment variable not set")
        return False
    
    print("✅ API Key found")
    
    # Initialize the system
    try:
        system = FlightMonitoringSystem()
        print("✅ Flight Monitoring System initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize system: {e}")
        return False
    
    # Test flight information
    flight_info = {
        "flight_number": "AC123",
        "aircraft_type": "Boeing 737",
        "origin": "Toronto",
        "destination": "Vancouver",
        "scheduled_departure": "2025-07-25T10:00:00Z"
    }
    
    # Test image URL (using the working image from your test)
    test_image_url = "https://ark-doc.tos-ap-southeast-1.bytepluses.com/see_i2v.jpeg"
    
    print(f"\n🛩️  Testing with flight: {flight_info['flight_number']}")
    print(f"📷 Image URL: {test_image_url}")
    
    # Analyze the image
    try:
        print("\n🔍 Analyzing flight image...")
        result = system.analyze_flight_image(test_image_url, flight_info)
        
        if result.get("status") == "error":
            print(f"❌ Analysis failed: {result.get('error')}")
            return False
        
        print("✅ Analysis completed successfully")
        
        # Display structured results
        print("\n📊 Analysis Results:")
        print("=" * 50)
        
        # Flight status
        status = result.get("flight_status", "unknown")
        print(f"Flight Status: {status}")
        
        # Aircraft info
        aircraft = result.get("aircraft_info", {})
        print(f"Aircraft Type: {aircraft.get('type', 'unknown')}")
        print(f"Registration: {aircraft.get('registration', 'unknown')}")
        print(f"Operator: {aircraft.get('operator', 'unknown')}")
        
        # Environment
        env = result.get("environment", {})
        print(f"Weather: {env.get('weather', 'unknown')}")
        print(f"Visibility: {env.get('visibility', 'unknown')}")
        print(f"Time of Day: {env.get('time_of_day', 'unknown')}")
        
        # Safety
        safety = result.get("safety", {})
        print(f"Safety Concerns: {safety.get('concerns', 'none')}")
        print(f"Operational Status: {safety.get('operational_status', 'unknown')}")
        
        # Location
        location = result.get("location", {})
        print(f"Airport: {location.get('airport', 'unknown')}")
        print(f"Runway: {location.get('runway', 'unknown')}")
        
        # Operations
        ops = result.get("operations", {})
        print(f"Flight Phase: {ops.get('flight_phase', 'unknown')}")
        print(f"Ground Operations: {ops.get('ground_operations', 'unknown')}")
        
        # Confidence
        confidence = result.get("confidence_score", 0.5)
        print(f"Confidence Score: {confidence:.2f}")
        
        # Export results
        filename = system.export_results(result, "test_flight_analysis.json")
        print(f"\n💾 Results exported to: {filename}")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed with exception: {e}")
        return False

def test_sequence_monitoring():
    """Test sequence monitoring functionality"""
    print("\n🔄 Testing sequence monitoring...")
    
    system = FlightMonitoringSystem()
    
    # Mock sequence of images (replace with actual flight image URLs)
    image_sequence = [
        "https://ark-doc.tos-ap-southeast-1.bytepluses.com/see_i2v.jpeg",
        "https://ark-doc.tos-ap-southeast-1.bytepluses.com/see_i2v.jpeg",  # Same image for testing
    ]
    
    flight_info = {
        "flight_number": "AC456",
        "aircraft_type": "Airbus A320",
        "origin": "Montreal",
        "destination": "Calgary"
    }
    
    try:
        print("📸 Analyzing image sequence...")
        sequence_result = system.monitor_flight_sequence(image_sequence, flight_info)
        
        print("✅ Sequence analysis completed")
        
        # Display summary
        summary = sequence_result.get("monitoring_summary", {})
        print(f"\n📈 Monitoring Summary:")
        print(f"Total Images: {summary.get('total_images_analyzed', 0)}")
        print(f"Safety Concerns: {summary.get('safety_concerns_count', 0)}")
        print(f"Average Confidence: {summary.get('average_confidence', 0):.2f}")
        
        recommendations = summary.get("recommendations", [])
        if recommendations:
            print(f"Recommendations: {', '.join(recommendations)}")
        
        # Export sequence results
        filename = system.export_results(sequence_result, "sequence_monitoring_results.json")
        print(f"💾 Sequence results exported to: {filename}")
        
        return True
        
    except Exception as e:
        print(f"❌ Sequence monitoring failed: {e}")
        return False

def main():
    """Main test function"""
    print("🚁 Flight Monitoring System Test Suite")
    print("=" * 50)
    
    # Test basic functionality
    basic_success = test_basic_functionality()
    
    # Test sequence monitoring
    sequence_success = test_sequence_monitoring()
    
    # Summary
    print("\n" + "=" * 50)
    print("📋 Test Summary:")
    print(f"Basic Functionality: {'✅ PASS' if basic_success else '❌ FAIL'}")
    print(f"Sequence Monitoring: {'✅ PASS' if sequence_success else '❌ FAIL'}")
    
    if basic_success and sequence_success:
        print("\n🎉 All tests passed! Flight monitoring system is working correctly.")
    else:
        print("\n⚠️  Some tests failed. Please check the error messages above.")

if __name__ == "__main__":
    main() 