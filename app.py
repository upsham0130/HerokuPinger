import time, threading, http.client, json

WAIT_SECONDS = 300
connStrings = ['mm19bot.herokuapp.com', 'mm19survey.herokuapp.com', 'sadhanahelperapi.herokuapp.com', '']

def makeConn(connString):
    conn = http.client.HTTPSConnection(connString)
    headers = {'Content-type': 'application/json'}
    params = {"caffeinate" : "la colombe"}
    json_data = json.dumps(params)
    conn.request('POST', '/caffeinate', json_data, headers)
    response = conn.getresponse()
    print(response.read().decode())
    conn.close()
    threading.Timer(WAIT_SECONDS, index).start()

def index():
    makeConn(connStrings[0])
    makeConn(connStrings[1])
    makeConn(connStrings[2])

if __name__ == '__main__':
    index()