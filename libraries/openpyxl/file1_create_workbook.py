"""
reference: https://openpyxl.readthedocs.io/en/stable/tutorial.html
"""
from openpyxl import Workbook, load_workbook
from openpyxl.styles import PatternFill

"""
Creating a workbook and save to a file
"""


def print_workbook_sheets(workbook):
    for sheet_name in workbook.sheetnames:
        print(f"${sheet_name}")

    for sheet in workbook:
        print(f"sheet name: {sheet.title}")


workbook_file_path = '../../resources/people.xlsx'
workbook = Workbook()

# retrieve the active workbook
active_worksheet = workbook.active
workbook.remove(active_worksheet)

people_sheet = workbook.create_sheet(title="People", index=0)
print_workbook_sheets(workbook)

people_sheet["A1"] = "Name"
people_sheet["B1"] = "Age"

people_sheet["A1"].fill = PatternFill("solid", fgColor="DDDDDD")
people_sheet["B1"].fill = PatternFill("solid", fgColor="DDDDDD")

for row in people_sheet:
    for cell in row:
        print(f"value = {cell}")

workbook.save(workbook_file_path)

"""
Loading a spreadsheet file
"""
loaded_workbook = load_workbook(workbook_file_path, False)
print_workbook_sheets(loaded_workbook)