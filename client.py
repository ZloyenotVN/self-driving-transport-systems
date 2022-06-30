import websocket
import json
import time
import asyncio


async def dialog(ws,x,N=100):
    for i in range(N):
        x['data'] = {"UWB": [0, 1, i]}
        await ws.send(f"{json.dumps(x)}")

def on_message(ws, message):
    print('prishlo')
    data = json.loads(message)
    print('Сообщение')
    print(message)
    if data["action"] == "Login":
        dialog(ws,x=massIN)
        print('Success')

def on_error(ws, error):
    # print("Ошибка")
    # print(error)
    pass


def on_close(ws):
    print("### closed ###")
    ws.close()


def on_open(ws):
    ws.send('{"action":"Login","login":"mathName"}')


if __name__ == "__main__":
    massIN = {"action":"Send2Math","data":{"UWB": [0, 1, 2]}}
    websocket.enableTrace(True)
    input = websocket.WebSocketApp("ws://10.3.168.123:9000",
                                on_open=on_open,
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)


    input.run_forever()
