


import matplotlib.pyplot as plt
#to set the legends patches lib is used
import matplotlib.patches as mpatches
import pandas as pd
#to read excel files first install openpyxl libraby in python
#pip install openpyxl
#afetr installing use read_excel to read excel file
#when we have multiple sheets in excel ,we want to read on particular sheet give sheet_name
#usecols is used to select particular cols in excel spreadsheet
ds=pd.read_excel("C:\\Users\\pravallika\\Downloads\\telugu-dashboard-blank.xlsx",sheet_name='Data')#usecols="A,E")
#print(ds.to_string())

#marker is the style of axis
#marker color is called mec is used to color the axis in graph
plt.plot(ds['Country'],ds['Amount'],marker='*',mec='y')
plt.xlabel('COUNTRY',color='red')
plt.ylabel('Amount',color='red')
plt.title('SALES GRAPH',loc='center',color='blue')
b= mpatches.Patch(color='blue', label='country')
r = mpatches.Patch(color='red', label='Amount')
#to set the direction of legend use loc attribute
plt.legend(handles=[b,r],loc='upper right')
plt.show()

plt.barh(ds['Product'],ds['Amount'],color='red')
#plt.bar(ds['Product'],ds['Amount'],color='red')
plt.xlabel('PRODUCT',color='blue')
plt.ylabel('AMOUNT',color='blue')
plt.title('product sales',color='yellow')
p=mpatches.Patch(color='pink',label='PRODUCT')
o=mpatches.Patch(color='orange',label='Amount')
plt.legend(handles=[p,o])
plt.show()


plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
