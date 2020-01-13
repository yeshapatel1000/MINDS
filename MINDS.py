#written by Yesha Patel
from bs4 import BeautifulSoup
import csv
import requests
page = requests.get("https://en.wikipedia.org/wiki/2019_in_spaceflight#Orbital_launches")
soup = BeautifulSoup(page.content,'html.parser')
dates = []
table = soup.find('table', class_='wikitable')
dict = {}
element = ''
for rows in table.find_all('tr'):
    
    li = []
    col = rows.find_all('td')
    if len(col) == 5:
        ele = [e.text.strip() for e in col]
        if ele!='':
            ind = ele[0].index('[')
            
            element = ele[0][:ind]
        else:
            element = element
    if len(col) == 6:
        ele = [e.text.strip() for e in col]
        li.append(ele[5])
   
    if element not in dict:
        dict[element] = li
    else:
        dict[element].append(li)
print(dict)
dict2 = {}
list1 = []
count = 0
for i,j in dict.items():
    
    list1 = j
    
    if ['Operational'] in list1:
        count = count+1
    if ['Successful'] in list1:
        count = count+1
    if ['En route'] in list1:
        count = count+1
    dict2.update({i:count})
    count = 0
flag = 0
myFile = open('Example_output.csv','w')
with myFile:
    writer = csv.writer(myFile)
    line = ['date,','value']
    writer.writerow(line)
    for i,j in dict2.items():
        date = i
        date = date.split(" ")
        if len(date) == 2:
            timing = date[1].split(':')
            for k in range(len(timing[0])):
                if timing[0][k].isdigit():
                    flag = k
                    break
            if flag:
                timing[0] = timing[0][flag:]
            if len(timing) == 2:
                timing.append('00')
            if timing[0] == '' or timing[0].isalpha():
        
                timing.append('00')
                timing.append('00')
                timing.append('00')

            if 'January' in date[1]:
                j = str(j)
                res = ['2019-01-'+date[0]+'T'+timing[0]+":"+timing[1]+":"+timing[2]+"+00:00,",str(j)]
            if 'February' in date[1]:
                res = ['2019-02-'+date[0]+'T'+timing[0]+":"+timing[1]+":"+timing[2]+"+00:00,",str(j)]
            if 'March' in date[1]:
                res = ['2019-03-'+date[0]+'T'+timing[0]+":"+timing[1]+":"+timing[2]+"+00:00,",str(j)]
            if 'April' in date[1]:    
                res = ['2019-04-'+date[0]+'T'+timing[0]+":"+timing[1]+":"+timing[2]+"+00:00,",str(j)]
            if 'May' in date[1]:
                res = ['2019-05-'+date[0]+'T'+timing[0]+":"+timing[1]+":"+timing[2]+"+00:00,",str(j)]
            if 'June' in date[1]:
                res = ['2019-06-'+date[0]+'T'+timing[0]+":"+timing[1]+":"+timing[2]+"+00:00,",str(j)]
            if 'July' in date[1]:
                res = ['2019-07-'+date[0]+'T'+timing[0]+":"+timing[1]+":"+timing[2]+"+00:00,",str(j)]
            if 'August' in date[1]:
                res = ['2019-08-'+date[0]+'T'+timing[0]+":"+timing[1]+":"+timing[2]+"+00:00,",str(j)]
            if 'September' in date[1]:
                res = ['2019-09-'+date[0]+'T'+timing[0]+":"+timing[1]+":"+timing[2]+"+00:00,",str(j)]
            if 'October' in date[1]:
                res = ['2019-10-'+date[0]+'T'+timing[0]+":"+timing[1]+":"+timing[2]+"+00:00,",str(j)]
            if 'November' in date[1]:
                res = ['2019-11-'+date[0]+'T'+timing[0]+":"+timing[1]+":"+timing[2]+"+00:00,",str(j)]
            if 'December' in date[1]:
                res = ['2019-12-'+date[0]+'T'+timing[0]+":"+timing[1]+":"+timing[2]+"+00:00,",str(j)]
            writer.writerow(res)
