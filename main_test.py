import main
import orjson



#test 3 different sizes of input
# run this test with pytest main_test.py -s
def test_main_S():
    f = open("tests/output/t_outputS.json", "r")
    output = f.read()
    x = orjson.loads(output)
    print(f"\n\n\n", '{:-^50}'.format('small output file'))
    print("\noutput file: \n", output)

    main.main("tests/output/t_outputS.json")
    f = open("tests/records/t_recordsS.json", "r")
    output = f.read()
    
    x = orjson.loads(output)
    f = open("records.json", "r")
    output = f.read()
    y = orjson.loads(output)
    print("records file produced: \n", output)
    if x == y:
        print("test passed!")
    assert(x == y)

def test_main_M():
    main.main("tests/output/t_outputM.json")
    f = open("tests/records/t_recordsM.json", "r")
    output = f.read()
    x = orjson.loads(output)
    f = open("records.json", "r")
    output = f.read()
    y = orjson.loads(output)
    print(f"\n\n", '{:-^50}'.format('medium output file'))
    if x == y:
        print("test passed!")

    assert(x == y)

def test_main_L():
    main.main("tests/output/t_outputL.json")
    f = open("tests/records/t_recordsL.json", "r")
    output = f.read()
    x = orjson.loads(output)
    f = open("records.json", "r")
    output = f.read()
    y = orjson.loads(output)
    print(f"\n\n", '{:-^50}'.format('large output file'))
    if x == y:
        print("test passed!")
    assert(x == y)
