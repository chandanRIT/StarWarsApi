import os

import socketio


class SocketClient:

    def __init__(self, host_url, timeout):
        self.results = []
        self.errors = []
        self.timeout = timeout
        self.host_url = host_url

    # does substring match based on the query string, returns a pair of results and errors.
    def search(self, query):
        self.results = []
        self.errors = []

        with socketio.SimpleClient() as client:
            client.connect(self.host_url, transports=['websocket'])
            client.emit('search', {'query': query})

            _, first_data = client.receive(timeout=self.timeout)
            total_rows = first_data["resultCount"]
            print(f'Total rows expected: {total_rows} {os.linesep}')

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

