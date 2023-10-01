import orjson # library for fast json parsing



# main function that takes in a file path pointing to a json file of START and END events. Writes a json file of summary records
def main(outputFilePath: str):
    f = open(outputFilePath, "r")
    output = f.read()
    data = orjson.loads(output)
    coll = {}
    records = []

    #O(n) time complexity
    # the algorithms processes pairs of records and creates a new summary record
    for i in range(len(data)):  
        # if the id is already in the collection, then we have a pair of events
        if data[i]["id"] in coll:
            start = data[coll[data[i]["id"]]]
            end = data[i]
            record = {
                "sessionId": start["id"],
                "sessionStartTime": start["timestamp"],
                "sessionEndTime": end["timestamp"],
                "sessionDuration": int(end["timestamp"]) - int(start["timestamp"]),
                "returnedLate": True if int(end["timestamp"]) - int(start["timestamp"]) > 86400 else False, # 86400 seconds in a day
                "damaged": True if end["comments"] != "" else False
            }
            records.append(record)
            del coll[data[i]["id"]]
        #add the id to the collection
        else: 
            coll[data[i]["id"]] = i

    #write list of summary records to a file. 
    d = orjson.dumps(records)
    with open("records.json", "wb") as f:
        f.write(d)

if __name__ == "__main__":
    main()

#Written By Quinten Bruce on 10/1/2023
