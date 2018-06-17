import csv


def emp_read(filename='/Users/su/Documents/Ilya/staff-load-tests/Workbook1.csv'):
    """
    Reads Employees information from file
    returns dictionary of Employee records with Guid keys

    :param filename: name of the file containing Employees data in CSV format
    :return: a dictionary of Employee records with Guid keys
    """
    empdict = dict()
    with open(filename, 'rU') as Emp_file:
        employeesd = csv.DictReader(Emp_file, dialect="excel")
        for row in employeesd:
            empdict[row['Guid']] = row
    return empdict


def emp_write(filename='/Users/su/Documents/Ilya/staff-load-tests/employees.csv'):
    """

    :param filename:
    :return:
    """

if __name__ == "__main__":
    EMP = emp_read()
    for i in EMP.keys():
        print EMP[i]
