from urllib.request import urlopen
import json
import pandas as pd

api_key = '1733ab538ef24bc29d5e6b329f28da89'

url_1 = f"https://newsapi.org/v2/everything?q="
url_2 = f"&from=2021-06-16&sortBy=publishedAt&apiKey={api_key}"

rawDf = {
    'id':[],
    'name':[],
    'author':[],
    'title':[],
    'description':[],
    'url':[],
    'urlToImage':[],
    'publishedAt':[],
    'content':[]
}


class News:
   def __init__(self):
      self.fileName = "new_data.csv"

   def searchFor(self):
      print("Get News On The basics of Keyword")
      keyword = input("Enter a keyword ")
      self.scrapData(keyword)

   def scrapData(self,key):
      print("Getting Data...  ")
      data = json.loads(urlopen(url_1+key+url_2).read())
      self.extractData(data)
      

   def extractData(self,data):
      print("extracting data...")
      for meta in data['articles']:
          rawDf['id'].append(meta['source']['id'])
          rawDf['name'].append(meta['source']['name'])
                    
          for key in list(rawDf.keys())[2:]:
              rawDf[key].append(meta[key])
      self.createDataFrame(rawDf)
          
   def createDataFrame(self,rawDf):
      print("creating dataframe")
      df = pd.DataFrame(rawDf)
      self.loadDataInCsv(df)

   def loadDataInCsv(self,df):
      print("loading data in csv .....")
      df.to_csv(self.fileName)
      print(df)
      print("\nfile is saved!!")
      


n = News()
n.searchFor()













   
