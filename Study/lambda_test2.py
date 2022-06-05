files = input().split()
# 1.jpg 10.png 11.png 2.jpg 3.png
# 97.xlsx 98.docx 99.docx 100.xlsx 101.docx 102.docx
print(list(map(lambda x: x.zfill(4+len(x.split('.')[1])), files)))
print(list(map(lambda x: '{0:0>3}.{1}'.format(*x.split('.')), files)))
