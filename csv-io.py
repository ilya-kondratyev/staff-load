import csv
import os.path
import shutil


def emp_read(filename='/home/user/Documents/Ilya/staff-load-tests/Workbook1.csv'):
    """
    Reads Employees information from file
    returns dictionary of Employee records with Guid keys

    :param filename: name of the file containing Employees data in CSV format
    :return: a dictionary of Employee records with Guid keys
    """
    if os.path.isfile(filename): # check if file  exists
        empdict = dict()
        with open(filename, 'rU') as Emp_file:
            employees_reader = csv.DictReader(Emp_file, dialect="excel")
            for row in employees_reader:
                empdict[row['Guid']] = row
        return empdict


def emp_write(filename='/home/user/Documents/Ilya/staff-load-tests/employees.csv', empdict = {}):
    """
    Writes Employees information to file. if the file already exists then makes .bak backup and overwrites
    :param filename: name of the file to store the Employees data in CSV format
           empdict: dictionary of Employee records with Guid keys
    :return: returns 0 if the new file was created, 1 if the file was overwritten and 2 on error
    """
    result = 0
    try:
        if os.path.isfile(filename):
            shutil.copyfile(filename, filename + '.bak')  # check if file already exists and make a copy
            result = 1
        with open(filename, 'w') as Emp_file:
            employees_writer = csv.DictWriter(Emp_file,fieldnames=empdict['1'].keys())
            employees_writer.writeheader()
            for guid in empdict.keys():
                employees_writer.writerow(empdict[guid])
            return result
    except:
        result = 2
        return result


if __name__ == "__main__":
    EMP = emp_read()
    for i in EMP.keys():
        print EMP[i]
    print emp_write(empdict = EMP)

