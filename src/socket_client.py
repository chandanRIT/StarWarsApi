import socketio


class SocketClient:
    HOST_URL = 'http://localhost:3000'
    TIMEOUT_SECONDS = 10

    def __init__(self, timeout):
        self.results = []
        self.errors = []
        self.timeout = timeout

    def search(self, query):
        self.results = []
        self.errors = []

        with socketio.SimpleClient() as client:
            client.connect(SocketClient.HOST_URL, transports=['websocket'])
            client.emit('search', {'query': query})

            _, first_data = client.receive(timeout=self.timeout)
            total_rows = first_data["resultCount"]
            print(f'Total number of rows to expect: {total_rows}')

            self.process_data(first_data)

            for i in range(1, total_rows):
                _, data = client.receive(timeout=self.timeout)
                self.process_data(data)

        return self.results, self.errors

    def process_data(self, data):
        if "error" in data:
            print(f'error is {data["error"]}')
            self.errors.append(data["error"])

        else:
            i = data["page"]
            row = {"name": data["name"], "films": data["films"]}
            print(f'row {i}: {row}')
            self.results.append(row)

