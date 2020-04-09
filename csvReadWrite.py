
import csv

#Append
with open('employee_file2.csv', mode='a') as csv_file:
    append = csv.writer(csv_file)

#Read
with open('employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')



def appendCatalog(title, authorName, authorAge, ISBN):
    with open('Catalog.csv', mode='a') as Catalog:
        append = csv.writer(Catalog)
    append.writerow([title, authorName, authorAge, ISBN])

def appendloanAdministration():
    with open('Catalog.csv', mode='a') as Catalog:
            append = csv.writer(Catalog)
        append.writerow([])

def appendloanItem():
    with open('Catalog.csv', mode='a') as Catalog:
            append = csv.writer(Catalog)
        append.writerow([])

def appendPerson():
    with open('Catalog.csv', mode='a') as Catalog:
            append = csv.writer(Catalog)
        append.writerow([])

def readCatalog():
    with open('Catalog.csv', mode='r') as Catalog:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')

def readloanAdministration():


def readloanItem():


def readPerson():