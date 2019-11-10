import pprint
import xlrd

d = {}
wb = xlrd.open_workbook('wods.xlsx')
sh = wb.sheet_by_index(0)

def makeDictionary():
    for i in range(1,117660):
        pos_value = float(sh.cell(i,0).value)
        neg_value = float(sh.cell(i,1).value)
        words = sh.cell(i,2).value
        for word in words.split():
            d[word[:-2].replace('_',' ')] = 1 - (pos_value + neg_value)
        

    return d
