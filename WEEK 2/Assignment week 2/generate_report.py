#!/usr/bin/env python3
import csv

def read_employees(csv_file_path):
    csv.register_dialect('empDialect',skipinitialspace=True,strict=True)
    employee_file = csv.DictReader(open(csv_file_path),dialect='empDialect')
    employee_list=[]
    for data in employee_file:
        employee_list.append(data)
    return employee_list

employee_list = read_employees('/home/student-01-cec10806837f/data/employees.csv')

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

dictionary = process_data(employee_list)

def write_report(dictionary,report_file):
    with open(report_file,"w+") as file:
        for record in sorted(dictionary):
            file.write(str(record)+':'+str(dictionary[record])+'\n')
        file.close()

write_report(dictionary,"/home/student-01-cec10806837f/data/report.txt")

