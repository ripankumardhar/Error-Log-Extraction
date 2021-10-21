

#Read Input Log File
infile = "/home/ripan/Desktop/logfiles/pythonProject/loginput.txt"

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





