# Kochi-STAMP-Data-Challenge
With the Problem Statement of Kochi for All - we considered the problem of the Crowd at the metro station that affects the travel plan of a person.
We extracted information about the no. of people(crowd) at the station in the intervals of half and hour for everyday of the week using Ticketing dataset's and Analaysing no. of Tickets booked in the intervals of half and hour.

We have created a Web Application using flask that takes inputs from the user and Tells him the probable crowd at the metro station during that time,so that he can plan his journey well.

The Main Target Audience for this application are Elderly citizens and differently abled peoples. 

### Working 
* Install Python and pip in open windows powershell using python website

* Install Virtualenv by:
 ``` pip install virtualenv
 ```
* open windows powershell and create a virtual environment using virtualenv :
```
   virtualenv venv 
```
* Keep all these files in the venv folder and move to scripts folder and activate virtual environment:

```
   1) cd Scripts
   2) .\activate
```
* Then Install Necessary packages like :

```
   flask - pip install flask
   pandas - pip install pandas
   matplotlib - pip install matplotlib
   datetime - pip install datetime
```
* Then move to the app folder on the powershell and type command to launch the flask web app :

```
  cd ..
  cd app
  python app.py
```

* Now your local server will be running at http://127.0.0.1:5000/ open the browser and type this link there and add send at the end
  soo that it will be - http://127.0.0.1:5000/send on the browser and press enter
 
* You will be navigated to page like this  -
  ```
 ![Screenshot (101)](https://user-images.githubusercontent.com/37475805/54507965-ce1e5980-4969-11e9-8104-ab8700f555e8.png)
```
* Enter the The inputs and click submit you will get the the the entire days crowd details like this - 
 ```
 
![Screenshot (105)](https://user-images.githubusercontent.com/37475805/54508022-29e8e280-496a-11e9-8b62-d3511ab4fbed.png)

```
  
  
