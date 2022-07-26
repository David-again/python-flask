# Markdown 101.
#### A boilerplate markdown 
_______
### Read this first!
A brief, introductory paragraph about the project goes here.
 `Code snippet`
 e.t.c., e.t.c., e.t.c `.json` file.

#### Content of this ReadMe file
0. Package contents
1.	How to run - General information
1.1 Automated processing
1.2 Manual processing
2.	Input file format
    - Notes
    - Assumptions
3.	Output
4.	Test Cases
5.	Performance
6.	Limitations
7.	Future work
8.	Comments and conclusion


## 0. Package contents
This package should consist of at least the following items:
Filename | Description
-|- 
`"README.md"` | This read-me file, providing a usage overview
`"MainScript.py"` | Script written in Python for processing the `.csv` file
`"ManualTest.py"` | Script written for ManualTest procedure, to be used with data files.
`"output.json"` | Output file for the result of processing.  A new one is created when `MainScript.py` is run.
`"data/sampledata1.csv"` | The main input file supplied with this package
`"data/sample_####recs.csv"` | Input file(s) supplied for test cases
`"Documentation/DesignDoc.md"` | Design document, providing a high-level, quasi-technical description of the software from a design viewpoint
`"Documentation/ReleaseTestPlan.md"` | General description of the Test Procedures (including Manual Testing)

Additionally, it MAY contain the following, although they can be generated from the above list.

Filename | Description
-|-
`"Notebook_MainScript.ipynb"` | Same Script written in Jupyter Notebooks format, if preferred.
`"test-output.json"` | Output file for the result of processing.  A new one is created when `ManualTest.py` is run.


**Note:**

`output.json` and `test-output.json` are created or overwritten every time the `MainScript.py` and `ManualTest.py` (respectively) are run.  Initially, there is no `test-output.json` file.

## 1. How to run - General information
**1.1** For automated processing, use `MainScript.py`.  The input file path is parameterized in a variable at the top, and can be changed for manual testing.

    `datafile_path = "data/sampledata1.csv"      #change input file here`

**1.2** For manual processing, please use `ManualTest.py`



**Notes**
- `ManualTest.py` requires both an input file `(.csv)` and the target address of the aircraft for which the test is being conducted.
- Please see the `ReleaseTestPlan.md` for more details (including Manual Test Procedures).


## 2. Input file format

The input file `(.csv)` should contain 2 fields per line: the time and target address of each aircraft.
`Time` | `Input String`
-|- 
`"2022-02-12 12:00:17.zzz"` | `"ABCDEF"`
**Notes**
- Note 1
- Note 2
- Note 3
- Note 4

**Assumptions**
- There are no invalid data in the input file
- There are no null fields in the input file

## 3. Output 

The output is presented in JSON format.  See example below.  

`{
    "someKey": "someValue", 
    "anotherKey": 3.5, 
    "finalKey": 7 
}`



## 4. Test Cases

Please consult the `ReleaseTestPlan.md` for details about testing and creating/substituting test cases.

## 5. Performance
Run-time will vary with the number of ***unique*** bla, bla, bla.  This is because the algorithm involves iterating as many times as the number of unique target address.  Therefore, performance is **`O(N)-time`**.

## 6. Limitations
Please review the following sections above: 
- **Notes** in the **Input file format** section.
- **Assumptions** in the **Input file format** section.
- Performance

## 7. Future work

This script/program can be easily expanded, depending on the desired output fields.

## 8. Comments and Conclusion
Python (and Pandas) was chosen for this project because of its data manipulation and analysis capabilities for the complexities described above, but comments, input and feedback are welcome.

>Thank you for taking the time to review my work.  I hope to hear from you soon, eager to answer any questions!
(c) 2022 David Ogunbanjo
d.ogunbanjo@yahoo.com