import socketio


class SocketClient:
    HOST_URL = 'http://localhost:3000'

    def __init__(self):
        self.results = []
        self.errors = []

    def search(self, query):
        self.results = []
        self.errors = []

        with socketio.SimpleClient() as sio:
            sio.connect(SocketClient.HOST_URL, transports=['websocket'])
            sio.emit('search', {'query': query})

            first_event = sio.receive()
            _, first_data = first_event
            # print(f'received first event with data: "{first_data}')

            total_rows = first_data["resultCount"]
            print(f'Total number of rows to expect: {total_rows}')

            self.collect_data(first_data)

            for i in range(1, total_rows):
                event = sio.receive()
                _, data = event
                self.collect_data(data)

        return self.results, self.errors

    def collect_data(self, data):
        if "error" in data:
            print(f'error is {data["error"]}')
            self.errors.append(data["error"])
        else:
            i = data["page"]
            row = {"name": data["name"], "films": data["films"]}
            print(f'row {i}: {row}')
            self.results.append(row)

