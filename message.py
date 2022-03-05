import http.client

def getMotiMessage():
    conn = http.client.HTTPSConnection("motivational-quotes1.p.rapidapi.com")

    payload = "{\n    \"key1\": \"value\",\n    \"key2\": \"value\"\n}"

    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "motivational-quotes1.p.rapidapi.com",
        'x-rapidapi-key': "bfce1ab576msh7ba183efa6c3bc7p19f616jsn9d5dafbaf327"
        }

    conn.request("POST", "/motivation", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    return(data.decode("utf-8"))
