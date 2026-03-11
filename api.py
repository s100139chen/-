import requests
import json

# 設定 Polygon.io API
# 建議將 API_KEY 替換為你在官網申請到的金鑰
API_KEY = "3nOLHpUEETTmwYAsqA4x4LRHrMQrRF3f"
URL = f"https://api.polygon.io/v2/aggs/ticker/AAPL/prev?adjusted=true&apiKey={API_KEY}"

def fetch_data():
    # 發送 GET 請求
    response = requests.get(URL)
    
    if response.status_code == 200:
        data = response.json()
        # 儲存為 JSON 格式 (符合作業要求)
        with open('stock_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("資料擷取成功！")
    else:
        print(f"錯誤碼：{response.status_code}")

if __name__ == "__main__":
    fetch_data()
