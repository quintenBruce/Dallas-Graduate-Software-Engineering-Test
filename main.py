import orjson

def main(fileName: str):
    f = open(fileName, "r")
    output = f.read()
    data = orjson.loads(output)
    coll = {}  # key:id, value:index
    records = []
    for i in range(len(data)):  # O(n) time complexity
        if data[i]["id"] in coll:
            if data[coll[data[i]["id"]]]["type"] == "START":
                start = data[coll[data[i]["id"]]]
                end = data[i]
            else:
                start = data[i]
                end = data[coll[data[i]["id"]]]
            record = {
                "sessionId": start["id"],
                "sessionStartTime": start["timestamp"],
                "sessionEndTime": end["timestamp"],
                "sessionDuration": int(end["timestamp"]) - int(start["timestamp"]),
                "returnedLate": True if int(end["timestamp"]) - int(start["timestamp"]) > 86400 else False,
                "damaged": True if end["comments"] != "" else False
            }
            records.append(record)
            del coll[data[i]["id"]]
        else:
            coll[data[i]["id"]] = i

    d = orjson.dumps(records)
    with open("records.json", "wb") as f:
        f.write(d)

if __name__ == "__main__":
    main()
