
# Dallas Graduate Software Engineering Test

Task: Develop an application that parses an output file and generates a summary record for each session.




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


## Run with Github Workflows

navigate to 
https://github.com/quintenBruce/Dallas-Graduate-Software-Engineering-Test/actions/workflows/python-app.yml. click on the latest workflow. Select re-run all jobs. This will produce an xml artifact that show the status of the tests. 




## Assumptions
I assumed that
- The output file may contain START events without corresponding END events, and vice versa.
- A START event occurs before its corresponding END event.
- The rental company needs the summary records in a new JSON file.

## Approach

Based on my assumptions, I created an O(n) time algorithm to process the events in the output file. My approach was to...
- Parse the output file into a Python array of dictionaries.
- Create a dictionary to store event id's and their array index.
- Iterate over the array of events, checking if each event's id is in the dictionary.
    - If the event id is in the dictionary, use the current event and the event pointed to by dictionary[id] to create a summary record. Append the record to the records array. Delete dictionary[id]
    - If the event id is not in the dictionary, add the id to the dictionary.
- Dump array of summary records to a file.
By using a dictionary to find event pairs, we can process events in O(n) time, where n is the number of events in the output file.

#### Other Approaches
I created a multiprocessing version of this program using the multiprocessing library. Theoretically, by spreading the load across n CPUs, the efficiency could be increased by a factor of n. In practice, however, I found that the cost of spinning up additional processes was more expensive than the reduction in total CPU wall clock time, causing the program to run 1.3 times slower on average than the serial version.

## Performance
This program can process large files quickly because of the O(n) time complexity. This program can process 12,000,000 events and write a records file in about 41s on my machine. I chose 12,000,000 events as an upper bound based on Avis, a car rental company. Avis has 1,631 locations in the U.S. Assuming they have 20 events per day, there are approximately 12,000,000 events in a year across all locations. I could not include this test in the repository due to the file size. \
**Additional Considerations**
- I used orjson to parse json data because of its performance benchmarks. It can parse data 40-50 times faster than other json parsing libraries.

## Future Iterations
Writing the summary records array to a file is the performance limiting factor in this approach. Depending on how the rental company needs the summary record data, I would consider alternatives to writing JSON to a file. If the company needs to access information about a specific record, then adding each record to a high performance database would be most efficient.
