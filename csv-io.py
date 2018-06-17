import csv

EmpDict=dict()
with open('/Users/su/Documents/Ilya/staff-load-tests/Workbook1.csv', 'rU') as Emp_file:

    Employeesd=csv.DictReader(Emp_file, dialect="excel")
    i=0
    for row in Employeesd:
        EmpDict[row['Guid']]=row
        i=i+1

print EmpDict


