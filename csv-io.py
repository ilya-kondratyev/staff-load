import csv
import os.path
import shutil

"""
Module crv_io.py contains functions to read and write Employees,Projects,Tasks,Teams information from/to CSV file
File format is the following
--------
Employees.csv
Guid,Name,Grade,TotalTokens,AvailableTokens,List_of_AssignedTasks (colon separated list of Task Guids ),List_of_Skills (colon separated list of Skills)
--------
Tasks.csv
Guid,Name,Requester,Project(Guid, can be empty),Employee(Guid), Workload (in work hours), 
Difficulty ( from 1 to 5), 
Requested_Start(date of initial request), 
Planned_Start(date planned to start), 
Effective_Start(date started to work on task),
Requested_Deadline(date from the requester), 
Planned_Deadline (date after effective start), 
OnHold (1 - yes or 0 -  no), 
Planned_Resume( date planned to resume after putting on hold),
Finished (1 - yes or 0 -  no)


"""

def csv_read(filename='~/Test.csv'):
    """
    Reads Employees,Projects,Tasks,Teams information from file
    returns dictionary of records with Guid keys
    :param filename: name of the file containing  data in CSV format
    :return: a dictionary of  records with Guid keys
    """
    if os.path.isfile(filename): # check if file  exists
        tempdict = dict()
        with open(filename, 'rU') as csv_file:
            records_reader = csv.DictReader(csv_file, dialect="excel")
            for row in records_reader:
                tempdict[row['Guid']] = row
        return tempdict


def csv_write(filename='~/Test.csv', tempdict = {}):
    """
    Writes Employees,Projects,Tasks,Teams information to file. if the file already exists then makes .bak backup and overwrites
    :param filename: name of the file to store the  data in CSV format
           tempdict: dictionary of  records with Guid keys
    :return: returns 0 if the new file was created, 1 if the file was overwritten and 2 on error
    """
    result = 0
    try:
        if os.path.isfile(filename):
            shutil.copyfile(filename, filename + '.bak')  # check if file already exists and make a copy
            result = 1
        with open(filename, 'w') as csv_file:
            records_writer = csv.DictWriter(csv_file,fieldnames=tempdict['1'].keys())
            records_writer.writeheader()
            for guid in tempdict.keys():
                records_writer.writerow(tempdict[guid])
            return result
    except:
        result = 2
        return result




if __name__ == "__main__":
    EMP = csv_read('~/Employees.csv')
    for i in EMP.keys():
        print EMP[i]
    print csv_write(filename='~/Employees.csv',tempdict= EMP)

