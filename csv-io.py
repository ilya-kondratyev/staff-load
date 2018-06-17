import csv


def EMP_READ(filename='/Users/su/Documents/Ilya/staff-load-tests/Workbook1.csv'):
    """Reads Employees infromation from file
    returns dictionary of Employee records with Guid keys
    """
    EmpDict=dict()
    with open(filename, 'rU') as Emp_file:
        Employeesd=csv.DictReader(Emp_file, dialect="excel")
        for row in Employeesd:
            EmpDict[row['Guid']]=row
    return EmpDict


if __name__== "__main__":
    EMP = EMP_READ()
    for i in EMP.keys():
        print EMP[i]
