import os
import json
from functools import reduce
import itertools
import xlsxwriter

path = "./data/tracker.json"




def view_generation(e):
    return {
        "outlet": e['outletIdentifier'],
        "brand": e['brand'],
        "completed": e['completed'],
    }

def make_sheet(items):
    workbook = xlsxwriter.Workbook('./dump/hello.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    platforms_view = map(view_generation, items)
    index = 1
    worksheet.write('B' + '1', 'outlet', bold)
    worksheet.write('C' + '1', 'brand', bold)
    worksheet.write('D' + '1', 'completed', bold)
    for platform in platforms_view:
        index = index + 1
        worksheet.write('B' + str(index), platform['outlet'])
        worksheet.write('C' + str(index), platform['brand'])
        worksheet.write('D' + str(index), platform['completed'],bold)
    workbook.close()


with open(path, 'r') as f:
    distros_dict = json.load(f)
    outlets = distros_dict['outlets']
    total = 0
    all_platforms =[]

    for outlet in outlets:
        platforms = outlets[outlet]  
        all_platforms = all_platforms + platforms
    
    #making a map function and not a list to pass
    platforms_complete = map(lambda a: a['completed'], all_platforms)

    make_sheet(all_platforms)

    #calculating the total
    total = reduce(lambda a,b: a + b, platforms_complete)
    print(total)
   


