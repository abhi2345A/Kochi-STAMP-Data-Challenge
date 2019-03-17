from flask import Flask,render_template,request,jsonify,url_for
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import time
from datetime import datetime
df = pd.read_csv('Ticket.csv')
from PIL import Image
import os
#import plotly
time1=[]
result1=[]
app = Flask(__name__,static_folder='C:\\Users\\dell\\Desktop\\flaskapp')
@app.route('/send',methods = ['GET' , 'POST'])
def send():
	if(request.method == 'POST'):
		station = request.form['station']
		Time = request.form['Time']
		day =request.form['Day']
		y = compute(station,Time,day)
		#fullname = os.path.join(app.config['abc'],'book_read.png')
		print(y)

		return render_template('location.html',y=y,Time=Time,time1=time1,result1=result1)

	return render_template('index.html')





def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset

def compute(Source,datetimee,day):
    #Source = "Palarivatom"
    List1 = ['Aluva','Ambattukavu','Changampuzha Park','Cochin University','Companypady','Edapally','JLN_Stadium','Kalamassery'
            'Kaloor','Lissie','M.G Road','Maharajas College','Palarivatom','Pathadipalam','Pulinchodu']

    
    # In[200]:


    def PlotCount(df19):
        grouper = pd.TimeGrouper(freq="30T")
        df19.index = df19.reset_index()['Transaction Time'].apply(lambda x: x - pd.Timestamp(x.date()))
        df19count = df19.groupby(grouper).count()

        df19count.drop(columns=['Station','Equipment Type','Equipment ID','Fare Media','Fare Product','Ticket/Card Number','Transaction Type','Date'],inplace=True)

        df19count['newcolumn'] = df19count.index

        plt.figure(figsize=(10,10))
        df19count['Transaction Time'].plot(kind='barh')
        plt.savefig('templates/book_read.png')
        #plotly.offline.plot(fig, filename='templates/name.html')

        df19count['newcolumn'] = pd.to_datetime(df19count['newcolumn'])
        df19count.rename(columns={'Transaction Time':'Count'},inplace=True)
        df19count.reset_index(inplace=True)

        #datetimee = '19-01-2018 21:10'
        #datetimee = pd.to_datetime(datetimee)
        def Rushcounter(datetimee):
            datetimee = pd.to_datetime(datetimee)
            (time,count)=(0,0)
            for y in df19count.index:
                if df19count.iloc[y,2].hour==datetimee.hour:
                    if df19count.iloc[y,2].minute<=datetimee.minute:
                        (Index,time,count)=(df19count.index,df19count.iloc[y,0],df19count.iloc[y,1])
                        print(df19count.iloc[y-1,0],df19count.iloc[y-1,1])
                        print(df19count.iloc[y+1,0],df19count.iloc[y+1,1])
                        
                        result1.append(indic(df19count.iloc[y-2,1]))
                        result1.append(indic(df19count.iloc[y-1,1]))
                        result1.append(indic(df19count.iloc[y+1,1]))
                        result1.append(indic(df19count.iloc[y+2,1]))
                        
                        time1.append(str(df19count.iloc[y-2,0]).split()[2])
                        time1.append(str(df19count.iloc[y-1,0]).split()[2])
                        time1.append(str(df19count.iloc[y+1,0]).split()[2])
                        time1.append(str(df19count.iloc[y+2,0]).split()[2])
                        print(result1)
                        print(time1) 

            return time,count
        
        def RushIndicator(datetimee):
            time,count = Rushcounter(datetimee)
            describe = df19count.describe()
            minn = describe['Count']['min']
            maxx = describe['Count']['max']
            average = describe['Count']['mean']
            low  = minn
            h    = maxx
            m    = average
            l1   = (minn+average)/2
            h1   = (average+maxx)/2

            if count>=low and count<l1:
                return 'Crowd is Small'
            elif count>=l1 and count<m:
                return 'Crowd is Moderate'
            elif count>=m and count<h1:
                return 'Crowd is Large'
            elif count>=h1 and count<h:
                return 'Crowd is Very Large'
        
        def indic(count):
        	print(type(count),count)
	        describe = df19count.describe()
	        minn = describe['Count']['min']
	        maxx = describe['Count']['max']
	        average = describe['Count']['mean']
	        low  = minn
	        h    = maxx
	        m    = average
	        l1   = (minn+average)/2
	        h1   = (average+maxx)/2

	        if count>=low and count<l1:
	            return 'Crowd is Small'
	        elif count>=l1 and count<m:
	            return 'Crowd is Moderate'
	        elif count>=m and count<h1:
	            return 'Crowd is Large'
	        elif count>=h1 and count<h:
	            return 'Crowd is Very Large'   
        return(RushIndicator(datetimee))




    def functionforSource(source,day):
        source['Transaction Time'] = pd.to_datetime(source['Transaction Time'],infer_datetime_format=True)
        #print(source.head(5))
        #source['Transaction Time'] = source['Transaction Time'].apply(lambda x: datetime_from_utc_to_local(x))
        if day=='Sunday':
        	df19  = source[source['Date']=='19-01-2018']
        elif day=='Monday':
        	df19  = source[source['Date']=='20-01-2018']
        elif day=='Tuesday':
        	df19  = source[source['Date']=='21-01-2018']
        elif day=='Wednesday':
        	df19  = source[source['Date']=='22-01-2018']
        elif day=='Thursday':
        	df19  = source[source['Date']=='23-01-2018']
        elif day=='Friday':
        	df19  = source[source['Date']=='24-01-2018']
        elif day=='Saturday':
        	df19  = source[source['Date']=='25-01-2018']
      

        return(PlotCount(df19))


    # In[201]:


    if Source in List1:
        Source_var  = df[df['Station']==Source]
        return(functionforSource(Source_var,day))
        
    else:
        return('Wrong Source station')

  




if __name__ == "__main__":
	#app.debug = True
	app.run()
    


