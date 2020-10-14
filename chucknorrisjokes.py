from urllib.request import urlopen
import csv
import pandas as pd
import json
import requests

k=[]
v=[]
with open("/Users/stutijain/Downloads/Test/ID.csv",'r') as file:
    info=file.readlines()
    info=[i[:-1] for i in info]
    info=info[1:]
    for id in info:
        api_url="http://api.icndb.com/jokes/{}".format(id)
        r=requests.get(api_url)
        a=r.content.decode('UTF-8')
        a=json.loads(a)
        b=a['value']['joke']
        k.append(int(id))
        v.append(b)
file.close()     
mydict={'ID':k,'Joke':v}
# print(mydict[0])
df=pd.DataFrame(mydict)
print(df)
df.to_csv('jokes.csv',index=False)
