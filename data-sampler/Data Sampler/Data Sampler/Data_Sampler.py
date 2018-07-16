from ws4py.client.threadedclient import WebSocketClient
import json

class DummyClient(WebSocketClient):
    def opened(self):
        print("opened")


    def closed(self, code, reason=None):
        print("Closed down"), code, reason

    def received_message(self, m):
        json_string=m.data
        parsed_json = json.loads(json_string)
        print(m)
        print(parsed_json)
        if parsed_json["signal"]==2:            
            floor_number = parsed_json["data"]["entity"]["meta"]["buildingFloor"]
            print(floor_number)
        if len(m) == 175:
            self.close(reason='Bye bye')

if __name__ == '__main__':
    try:
        ws = DummyClient('wss://api.usb.urbanobservatory.ac.uk/stream', protocols=['http-only', 'chat'])
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()
