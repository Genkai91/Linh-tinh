import requests
import time

url = "http://1.1HK.HKG7.837.E.194.165"  # Thay thế bằng URL thực tế

while True:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # Giả sử là JSON
        chosen_room = data.get("chosen_room")
        print(f"Sát thủ đã chọn vào phòng: {chosen_room}")
    time.sleep(5)  # Khoảng thời gian giữa các lần kiểm tra
