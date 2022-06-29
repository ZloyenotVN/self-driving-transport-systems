import websocket
import json

def on_message(ws, message):
    data = json.loads(message)
    print('Сообщение')
    print(data)

def on_error(ws, error):
    print("Ошибка")
    print(error)


def on_close(ws):
    print("### closed ###")
    ws.close()


def on_open(ws):
    # ws.send(
    #     "{\"action\":\"Login\",\"login\":\"mathLogin\",\"password\":\"%wPp7VO6k7ump{BP4mu2rm4w?p|J5N%P\",\"roomid\":\"1\"}")
    # ws.send(
    #     f'Дима лох')
    ws.send(json.dumps([0,1,2,3,4,5]))

if __name__ == "__main__":


    websocket.enableTrace(True)
    input = websocket.WebSocketApp("ws://10.3.168.123:9000",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)


    input.on_open = on_open
    input.run_forever()
