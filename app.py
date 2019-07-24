import time, threading, http.client, json

def index():
    WAIT_SECONDS = 300

    conn = http.client.HTTPSConnection('mm19bot.herokuapp.com')

    headers = {'Content-type': 'application/json'}

    params = {"caffeinate" : "la colombe"}
    json_data = json.dumps(params)

    conn.request('POST', '/caffeinate', json_data, headers)

    response = conn.getresponse()
    print(response.read().decode())
    #threading.Timer(WAIT_SECONDS, ping).start()
    conn.close()
    threading.Timer(WAIT_SECONDS, index).start()

if __name__ == '__main__':
    index()