import main
import orjson

def test_main_S():
    main.main("tests/output/t_outputS.json")
    f = open("tests/records/t_recordsS.json", "r")
    output = f.read()
    print(output)
    x = orjson.loads(output)
    f = open("records.json", "r")
    output = f.read()
    y = orjson.loads(output)
    assert(x == y)

def test_main_M():
    main.main("tests/output/t_outputM.json")
    f = open("tests/records/t_recordsM.json", "r")
    output = f.read()
    x = orjson.loads(output)
    f = open("records.json", "r")
    output = f.read()
    y = orjson.loads(output)
    assert(x == y)

def test_main_L():
    main.main("tests/output/t_outputL.json")
    f = open("tests/records/t_recordsL.json", "r")
    output = f.read()
    x = orjson.loads(output)
    f = open("records.json", "r")
    output = f.read()
    y = orjson.loads(output)
    assert(x == y)
