import os
import requests
import json

def test_api_directly():
    """直接使用 requests 测试 API"""
    api_key = os.environ.get("ARK_API_KEY")
    base_url = "https://ark.ap-southeast.bytepluses.com/api/v3"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # 测试数据
    data = {
        "model": "ep-20250725145324-xrkzm",
        "messages": [
            {"role": "user", "content": "Hello"}
        ]
    }
    
    try:
        print("发送请求到:", base_url)
        print("模型:", data["model"])
        print("请求头:", {k: v[:20] + "..." if k == "Authorization" else v for k, v in headers.items()})
        
        response = requests.post(
            f"{base_url}/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )
        
        print(f"状态码: {response.status_code}")
        print(f"响应头: {dict(response.headers)}")
        
        if response.status_code == 200:
            result = response.json()
            print("✓ 成功!")
            print("响应:", json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print("✗ 失败!")
            print("错误响应:", response.text)
            
    except Exception as e:
        print(f"请求异常: {e}")

if __name__ == "__main__":
    test_api_directly() 