from ws4py.client.threadedclient import WebSocketClient
import json

class DummyClient(WebSocketClient):
    def opened(self):
        def data_provider():
            for i in range(1, 200, 25):
                yield "#" * i

        self.send(data_provider())

        for i in range(0, 200, 25):
            print(i)
            self.send("*" * i)

    def closed(self, code, reason=None):
        print("Closed down"), code, reason

    def received_message(self, m):
        json_string=m.data
        parsed_json = json.loads(json_string)
        print(m)
        print(parsed_json)
        if len(m) == 175:
            self.close(reason='Bye bye')

if __name__ == '__main__':
    try:
        ws = DummyClient('wss://api.usb.urbanobservatory.ac.uk/stream', protocols=['http-only', 'chat'])
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()

#import websocket
#import json

#try:
#    import thread
#except ImportError:
#    import _thread as thread
#import time

#def on_message(ws, message):
#    json_string=message
#    parsed_json = json.loads(json_string)
#    print(message)
    

#def on_error(ws, error):
#    print(error)

#def on_close(ws):
#    print("### closed ###")

#def on_open(ws):
#    def run(*args):
#        for i in range(3):
#            time.sleep(1)
#            ws.send("Hello %d" % i)
#        time.sleep(1)
#        ws.close()
#        print("thread terminating...")
#    thread.start_new_thread(run, ())


#if __name__ == "__main__":
#    websocket.enableTrace(True)
#    ws = websocket.WebSocketApp("wss://api.usb.urbanobservatory.ac.uk/stream",
#                              on_message = on_message,
#                              on_error = on_error,
#                              on_close = on_close)
#    ws.on_open = on_open
#    ws.run_forever()
