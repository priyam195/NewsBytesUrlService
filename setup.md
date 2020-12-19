This is a Python FLask application which is using reddis.
You can install python , flask and reddis in your local system

# setup

## 1. run a python virtual Enviroment in CMD
## 2. go to the NewsBytesURLServie/src directory
## 3. run command in cmd : flask run

## There are two end points

### 1. /hashURL endpoint
return 6 digit hash of long URL
it also returns the same hash for same URL.
and never return same hash for two diffrent URL


#### sample Input
{
   "url": "https://it.wikipedia.org/wiki/Commonwealth_delle_nazioni#Nazioni_del_Commonwealth_aventi_una_propria_monarchia_(6_stati)"
}
#### sample output
M2YxMm


### 2. /getHash  endpoint
accepts json and return hash of URL


#### sample Input
{
   "hash_of_url": "M2YxMm"
}
#### sample output
https://it.wikipedia.org/wiki/Commonwealth_delle_nazioni#Nazioni_del_Commonwealth_aventi_una_propria_monarchia_(6_stati)
