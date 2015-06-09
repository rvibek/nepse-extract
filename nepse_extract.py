import requests  
from pattern import web

postdata= {  
    'topTenBased' : '58', #value from Select menu (NEPSE) #57 Sensitive | #62 Float | #63 Sen Float
    'Submit' : 'Submit'
    }
r = requests.post('http://www.nepalstock.com/datanepse/Indices.php', data=postdata)  
dom = web.Element(r.text)

#Working with local file
# r = open('Indices.htm')
#dom = web.Element(r.read())

#creating DOM and getting the Title corresponding to topTenBased value
data = dom.by_tag('table.dataTable')[1]  
title = data.by_tag('td')[0].content  
title = title.partition(' ')[0] #title of the table


#Iteration and storing data in array 
def content (idx):  
    mydata = []
    for i in range(0, idx):
        ad=d.by_tag('td')[i].content
        mydata.append(ad)
    mydata.append(title)
    print mydata


for d in data.by_class('row1'):  
    idx = len(d.by_tag('td'))
    content(idx)