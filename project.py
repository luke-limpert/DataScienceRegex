#Case A - find all of the names in the following string
import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    name = re.findall('[A-Z]\w+', simple_string)
    return name

#Case B regex - make a list of students that received a B in the course
import re
def grades():
    with open ("grades.txt", "r") as file:
        grades = file.read()
        SortbyB = re.findall('[\w]*\s[\w]*: B', grades)
        for i in range(len(SortbyB)):
            SortbyB[i] = SortbyB[i].rstrip(': B')
        return SortbyB
print(grades())

#Case C regex - create a list of dictionaries where each dictionary looks like this
# example_dict = {"host":"146.204.224.152", 
#                 "user_name":"feest6811", 
#                 "time":"21/Jun/2019:15:45:24 -0700",
#                 "request":"POST /incentivize HTTP/1.1"}
import re
def logs():
    with open("logdata.txt", "r") as file:
        logdata = file.read()
    data = []
    pattern = '(?P<host>(?:\d+\.){3}\d+) - (?P<user_name>[-a-zA-Z0-9]*) [[\]](?P<time>[\d][\d][/][a-zA-Z]*[/][\d]*:[\d]*:[\d]*:[\d]* -[\d]*)[]] \"(?P<request>\w.+?)\"'
    j = re.finditer(pattern, logdata)
    for i in j:
        data.append(i.groupdict())
    return data
print(logs())