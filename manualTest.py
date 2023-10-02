import main
import sys

# test file name must be in tests/output
# must be a json file containing a list of START and END events
# run this test with python manualTest.py <filename of file in tests/output>
# if no filename is provided, then the test will run with the small output file
# example: python manualTest.py optional{t_outputS.json, t_outputM, t_outputL.json}
if len(sys.argv) < 2:
    main.main("tests/output/sample.json")
else:
    fileName = sys.argv[1]
    fileName = fileName.replace(".json", "")
    main.main(f"tests/output/{fileName}.json")

#inspect the records.json file to see the summary records