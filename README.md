# Error-Log-Extraction

The program consists code to monitor errors from a log file in given format:

2019-4-1 13:32:40 [190] User3 logs in 
2019-4-1 13:33:45 [123] User1 logs in 
2019-4-1 13:33:45 [123] User1 goes to search page 
2019-4-1 13:33:46 [123] User1 types in search text 
2019-4-1 13:33:48 [256] User2 logs in 
2019-4-1 13:33:49 [190] User3 runs some job 
2019-4-1 13:33:50 [123] User1 clicks search button
2019-4-1 13:33:53 [256] User2 does something 
2019-4-1 13:33:54 [123] ERROR: Some exception occured 
2019-4-1 13:33:56 [256] User2 logs off
2019-4-1 13:33:57 [190] ERROR: Invalid input

When errors occur, the log message will start with "ERROR:". 
The program scans the log file and generates a report in console with all errors. 
The order of the errors should follow the same order as the log file. 
Different sessions are seperated using "-----" as the separator between. 


Tests Covered : 

1. For each error, the report includes at most the last 3 messages for the same session before that error.
2. For each error with less than 3 messages before the error, the report includes all messages for the same session before that error along with comment as ¨// There are only no of messages before this error.¨
3. For each error without any user interaction before the error, the report includes error along with message ¨// No User actions found for this error ¨


```python

#Read Input Log File
infile = "C:/Readyapi Projects/loginput.txt"

#Declare Blank Lists to hold session ID and error phases
important = []
session = []
keep_phrases = ["ERROR:"]
max_lines_before_error = 3

#Read Input Log file
with open(infile) as f:
    f = f.readlines()

#Extract User session IDs for errors from log file
for line in f:
    for phrase in keep_phrases:
        if phrase in line:
            important.append(line)
            break

for line in important:
    session.append(line[line.index("[")+1:line.index("]")])
#print(session)


for phrase in session:
    listfile = []
    for line in f:
        if phrase in line:
          listfile.append(line)
    #print(listfile.__len__())
    count = listfile.__len__()
    if count == 1:
        print("\n".join(listfile))
        print("// No User actions found for this error ")
    if count <= max_lines_before_error & count > 1:
        print ("\n".join(listfile))
        print("// There are only ", count-1, " messages before this error")
    if count > max_lines_before_error:
        print ("\n".join(listfile[-4:]))
        print("// There are more than three messages before this error")

    print("--------------------------------------------------------------------------------------------------")

```

Console Output : 

```bash
2019-4-1 13:33:45 [123] User1 goes to search page 

2019-4-1 13:33:46 [123] User1 types in search text 

2019-4-1 13:33:50 [123] User1 clicks search button

2019-4-1 13:33:54 [123] ERROR: Some exception occured 

// There are more than three messages before this error
--------------------------------------------------------------------------------------------------
2019-4-1 13:33:48 [444] User4 logs in

2019-4-1 13:33:57 [444] ERROR: Invalid user

// There are only  1  messages before this error
--------------------------------------------------------------------------------------------------
2019-4-1 13:32:40 [190] User3 logs in 

2019-4-1 13:33:49 [190] User3 runs some job 

2019-4-1 13:33:58 [190] ERROR: Invalid Input

// There are only  2  messages before this error
--------------------------------------------------------------------------------------------------
2019-4-1 13:33:58 [555] ERROR: Invalid log

// No User actions found for this error 
--------------------------------------------------------------------------------------------------
2019-4-1 13:33:59 [447] User5 enters text

2019-4-1 13:33:59 [447] User5 clicks next

2019-4-1 13:34:03 [447] User5 clicks submit

2019-4-1 13:34:05 [447] ERROR: Page not available

// There are more than three messages before this error
--------------------------------------------------------------------------------------------------

Process finished with exit code 0



```



