# Dallas Graduate Software Engineering Test

Assignment: Develop an application that parses an output file and generates a summary record for each session.


## Repository Layout
**main.py** - The solution to the assignment\
**records.json** - The .json file produced by main.py that contains a list of summary records.  /
**manualTest.py** - Python file to manually test main.py. See https://github.com/quintenBruce/Dallas-Graduate-Software-Engineering-Test/tree/main#run-locally \
**main_test.py** - pytest file used to test main.test. See https://github.com/quintenBruce/Dallas-Graduate-Software-Engineering-Test/tree/main#run-locally \
**tests/output** - Folder containing json files used by main_test.py and manualTest.py to test main.py. \
**tests/records** - Folder containing the solutions to corrosponding files in tests/output. These files are used to verify the .json file produced by main.py\


## Run Locally

**Clone the project**

```bash
  git clone https://github.com/quintenBruce/Dallas-Graduate-Software-Engineering-Test
```

**Go to the project directory**

```bash
  cd Dallas-Graduate-Software-Engineering-Test
```

**Install dependencies**

```bash
  pip install orjson pytest
```

**Run tests**\
Running the main_test.py file will run 3 tests and print results of each test to the terminal. 

```bash
  pytest main_test.py -s
```

**Manually Test Program**\
Manually test the program against a file by running manualTest.py and optionally specifying the filename of a test located in tests/output/. The default is sample.json.

```bash
  python manualTest.py t_outputM #run program with tests/output/t_outputM.json
```
```bash
  python manualTest.py #run program with default tests/output/sample.json
```
Open the records.json file to see the summary records


## Run with Github Workflows

navigate to 
https://github.com/quintenBruce/Dallas-Graduate-Software-Engineering-Test/actions/workflows/python-app.yml. Click on the most recent workflow. Select rerun all jobs. This will produce an xml artifact showing the status of the tests. 




## Assumptions
I have assumed that
- The output file may contain START events without corresponding END events, and vice versa.
- A START event occurs before its corresponding END event.
- All events in the output file have the same fields.
- The rental company needs the summary records in a new JSON file.

## Approach

Based on my assumptions, I created an O(n) time algorithm to process the events in the output file. My approach was to...
- Parse the output file into a Python array of dictionaries.
- Create a dictionary to store event id's and their array index.
- Iterate over the array of events, checking if each event's id is in the dictionary.
    - If the event id is in the dictionary, use the current event and the event at index dictionary[id] to create a summary record. Append the record to the records array. Delete dictionary[id]
    - If the event id is not in the dictionary, add {id:index} to the dictionary.
- Dump array of summary records to a file.
By using a dictionary to find event pairs, we can process events in O(n) time, where n is the number of events in the output file.

#### Other Approaches
I created a multiprocessing version of this program using the multiprocessing library. Theoretically, spreading the load across n CPUs would increase efficiency. In practice, however, I found that the cost of spinning up additional processes was more expensive than the reduction in total CPU wall clock time, causing the program to run 1.3 times slower on average than the serial version.

## Performance
This program can process large files quickly because of the O(n) time complexity. This program can process 12,000,000 events and write a records file in about 41s on my machine. I chose 12,000,000 events as an upper bound based on Avis, a car rental company. Avis has 1,631 locations in the U.S. Assuming each location has 20 events per day, there are approximately 12,000,000 events in a year across all locations. I could not include this test in the repository because of the file size. \
**Additional Considerations**
- I used orjson to parse the json data because of its performance benchmarks. It can parse data 40-50 times faster than other json parsing libraries.

## Future Iterations
Writing the summary records array to a file is the performance limiting factor in this approach. Depending on how the rental company needs the summary record data, I would consider alternatives to writing JSON to a file. If the company needs to access information about a specific record, then adding each record to a high-performance database would be most efficient.\
If the output file size is large enough, it may be more efficient to run the main algorithm across many threads. However, the single-threaded version is more than adequate.\
In a realistic scenario, the events in the output file would have many more fields. I would adjust my algorithm accordingly, but the time complexity of the main algorithm would still be O(n). 
