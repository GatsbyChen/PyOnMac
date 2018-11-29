from openpyxl import load_workbook
import pandas as pd
import sys
sys.path.append('..\Dalian_Enterprise\InfoSheet')

df = pd.DataFrame()

header = []#表头有三十五列数据
with open("header.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    for i in lines[1:]:
        print(i.strip())
        header.append(i.strip())
print(header)

wb = load_workbook(r"InfoSheet.xlsx")
sh = wb["Sheet1"]
print(sh['T30'].value)
positionlist = []
with open("ExtractionPosition.txt","r+",encoding="utf-8") as f:
    lines = f.readlines()
    for i in lines:
        positionlist.append(i.strip())
print(positionlist)
infolist = []
print(sh[""+positionlist[1]+""].value)

EnterType = ["□中型","□小型","□微型","□中型","□小型","□微型"]
for i in range(47):
    for typ in EnterType:
        if sh[""+positionlist[i]+""].value != typ:
    # print(sh["" + positionlist[i] + ""].value)
            infolist.append(sh[""+positionlist[i]+""].value)
print(infolist)
# # print(list(zip(*positionlist)))
# infolist = []
# for i in positionlist:
#     infolist.append(sh[""+str(i)+""].value)
#     # print(type(sh[""+i+""].value))
#
# print(infolist)
# name = list(range(47))
# for i in header:
#     df[i] = [infolist[i]]
# #
# print(df)
# name = []
# # for i in list(range(47)):
# #     name.append(str(i))
# # name = ["1","2"]
# # print(name)
for i in range(35):
    df[header[i]] = [infolist[i]]
# #
print(df)

