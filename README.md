# NewsBytesUrlService
This service is used to convert long length URL to short 6 character hash
key is the hash 6 character hash and value is our URL.
The Idea is to use this hash instead of complete URL this will save space and also less chances of error by the user while copying or writing  it.
All users can maintain the hash instead of complte URL

## Hashing logic
### URL is encoded with md5hash which gives 32 chareters.
### This md5hash is further reduced to smaller length by encoding it to base64
### We use the first 6 charecter of it as our final hash
### Hash collision is also handled in the code by appending the url with string ("**")

eg https://newsbyteurl.com/M3gthf
the last 6 charecter can be of hash.

Reddis can we used as cache because it is in memeory. Reddis is also highly scalable in cloud enviroments. 


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


## The usage of Reddis Db 
You can have huge keys and values of objects as big as 512 MB, which means that Redis will support up to 1GB of data for a single entry 
which was  bascially help in storing large URLs
