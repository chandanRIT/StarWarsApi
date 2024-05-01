import os
import socketio


class SocketClient:
    def __init__(self, host_url, timeout):
        self.results = []
        self.errors = []
        self.timeout = timeout
        self.host_url = host_url

    def search(self, query):
        """
            Substring matches on character names and returns a pair of results and errors.
            Also prints the results and errors to the console.

            Parameters:
                query (str): The string used for substring search on character names.

            Returns:
                A pair of results and errors. Both are an array.
                Each result is a dictionary containing the matched character's name and their films.
                Each error is a string containing the error description.
        """

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

