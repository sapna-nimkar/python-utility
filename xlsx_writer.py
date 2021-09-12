import xlsxwriter
from random_utility import rand_name
from random_utility import rand_mobile

def create_xcel():
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook('sdet6.xlsx')
    worksheet = workbook.add_worksheet()
    print("worksheet created")

    #widen the first column to make text clearer

    worksheet.set_column('A:A', 20)

    #add a bold format to highlight cells

    bold = workbook.add_format({'bold': True})

    #write simple text worksheet
    worksheet.write('A1','firstname')
    worksheet.write('B1','lastname')
    worksheet.write('C1','mobile')

    return (workbook,worksheet)

    #insert phonebook data
def insert_info(worksheet, count = 1):
    column_num = 1
    for i in range(1,count+1):
        column_num = i + 1
        col_name_1 = f"A{column_num}"
        col_name_2 = "B"+str(column_num)
        col_name_3 = "C{}".format(column_num)  #you can also make a touple of all these 3

        worksheet.write(col_name_1,rand_name())
        worksheet.write(col_name_2,rand_name())
        worksheet.write(col_name_3,rand_mobile())
    

if __name__ == "__main__":
    workbook,worksheet=create_xcel()
    insert_info(worksheet,10)
    workbook.close()


