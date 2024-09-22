import websocket

def on_message(ws, message):
    print(f"Sát thủ đã chọn vào phòng: {message}")

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Đã đóng kết nối")

def on_open(ws):
    print("Kết nối thành công")

# Kết nối đến máy chủ WebSocket
ws = websocket.WebSocketApp("wss://98.98.194.178:443",
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever()
