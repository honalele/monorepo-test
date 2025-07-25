import os
import time
import requests
from openai import OpenAI

def test_connection():
    """测试基本连接"""
    print("=== 测试基本连接 ===")
    try:
        response = requests.get("https://ark.ap-southeast.bytepluses.com/api/v3", timeout=10)
        print(f"连接状态码: {response.status_code}")
        print("服务器可访问 ✓")
        return True
    except Exception as e:
        print(f"连接失败: {e}")
        return False

def test_api_with_curl():
    """使用 curl 测试 API"""
    print("\n=== 使用 curl 测试 API ===")
    api_key = os.environ.get("ARK_API_KEY")
    if not api_key:
        print("错误: 未找到 ARK_API_KEY")
        return False
    
    curl_cmd = f'''curl -X POST "https://ark.ap-southeast.bytepluses.com/api/v3/chat/completions" \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer {api_key}" \\
  -d '{{"model": "ep-20250725145324-xrkzm", "messages": [{{"role": "user", "content": "Hello"}}]}}' '''
    
    print("执行 curl 命令...")
    result = os.system(curl_cmd)
    return result == 0

def test_openai_client_with_retry(max_retries=3):
    """使用 OpenAI 客户端测试，带重试机制"""
    print("\n=== 使用 OpenAI 客户端测试 ===")
    
    api_key = os.environ.get("ARK_API_KEY")
    if not api_key:
        print("错误: 未找到 ARK_API_KEY")
        return False
    
    client = OpenAI(
        api_key=api_key,
        base_url="https://ark.ap-southeast.bytepluses.com/api/v3",
    )
    
    for attempt in range(max_retries):
        try:
            print(f"尝试 {attempt + 1}/{max_retries}...")
            
            completion = client.chat.completions.create(
                model="ep-20250725145324-xrkzm",
                messages=[
                    {"role": "user", "content": "Hello"}
                ],
                timeout=30
            )
            
            print("✓ 请求成功!")
            print(f"响应: {completion.choices[0].message.content}")
            return True
            
        except Exception as e:
            print(f"✗ 尝试 {attempt + 1} 失败: {type(e).__name__} - {str(e)}")
            
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # 指数退避
                print(f"等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
            else:
                print("所有重试都失败了")
                return False

def test_different_models():
    """测试不同的模型端点"""
    print("\n=== 测试不同的模型端点 ===")
    
    api_key = os.environ.get("ARK_API_KEY")
    if not api_key:
        print("错误: 未找到 ARK_API_KEY")
        return False
    
    # 常见的模型名称模式
    test_models = [
        "ep-20250725145324-xrkzm",  # 原始模型
        "gpt-3.5-turbo",            # 通用模型
        "gpt-4",                    # 另一个通用模型
    ]
    
    client = OpenAI(
        api_key=api_key,
        base_url="https://ark.ap-southeast.bytepluses.com/api/v3",
    )
    
    for model in test_models:
        try:
            print(f"测试模型: {model}")
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": "Hello"}
                ],
                timeout=10
            )
            print(f"✓ 模型 {model} 工作正常")
            return True
        except Exception as e:
            print(f"✗ 模型 {model} 失败: {str(e)}")
    
    return False

def main():
    print("BytePlus API 诊断工具")
    print("=" * 50)
    
    # 检查环境变量
    api_key = os.environ.get("ARK_API_KEY")
    if not api_key:
        print("❌ 错误: 未找到 ARK_API_KEY 环境变量")
        print("请设置环境变量: export ARK_API_KEY='your-api-key'")
        return
    
    print(f"✅ API Key 已设置: {api_key[:10]}...")
    
    # 运行各种测试
    tests = [
        ("基本连接", test_connection),
        ("OpenAI 客户端重试", test_openai_client_with_retry),
        ("不同模型测试", test_different_models),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        result = test_func()
        results.append((test_name, result))
    
    # 总结结果
    print(f"\n{'='*50}")
    print("测试结果总结:")
    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{test_name}: {status}")
    
    # 提供建议
    print(f"\n{'='*50}")
    print("建议:")
    if not any(result for _, result in results):
        print("1. 检查 API 密钥是否正确")
        print("2. 确认模型端点是否可用")
        print("3. 联系 BytePlus 技术支持")
        print("4. 检查网络连接")
    elif results[0][1] and not results[1][1]:
        print("1. 服务器可访问但 API 调用失败")
        print("2. 可能是模型端点问题")
        print("3. 尝试使用不同的模型名称")
    else:
        print("1. 部分功能正常工作")
        print("2. 可以继续使用可用的功能")

if __name__ == "__main__":
    main() 