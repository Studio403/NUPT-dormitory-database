import xlrd
import os

xls_list = []
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if ('.xls' in os.path.splitext(file)[1]):
           xls_list.append(file)

file=open("output.txt","w",-1,'utf-8')

for xls_file in xls_list:
    workbook = xlrd.open_workbook(xls_file)
    sheet_names= workbook.sheet_names()

    for sheet_name in sheet_names:
        print(sheet_name)
        building=workbook.sheet_by_name(sheet_name)
        row=3
        col=1
        while (row<building.nrows):
            if (building.cell(row,col).value!=""):
                room_id=building.cell(row,col).value
            bed_id=building.cell(row,col+1).value
            name=building.cell(row,col+2).value
            student_id=building.cell(row,col+3).value
            if (name!=""):
                str=f'{building.name},{room_id},{int(bed_id)},{name},{student_id}'
                #print(str)
                file.write(str+"\n")
            row=row+1

file.close()
print("Done.")