# NewsBytesUrlService
This service is used to convert long length URL to short 6 character hash
key is the hash 6 character hash and value is our URL.



## /hashURL endpoint
return 6 digit hash of long URL


### sample Input
{
   "url": "https://it.wikipedia.org/wiki/Commonwealth_delle_nazioni#Nazioni_del_Commonwealth_aventi_una_propria_monarchia_(6_stati)"
}
### sample output
M2YxMm


## /getHash  endpoint
accepts json ans return hash of URL

### sample Input
{
   "hash_of_url": "M2YxMm"
}
### sample output
https://it.wikipedia.org/wiki/Commonwealth_delle_nazioni#Nazioni_del_Commonwealth_aventi_una_propria_monarchia_(6_stati)


## The usage of Reddis Db 
You can have huge keys and values of objects as big as 512 MB, which means that Redis will support up to 1GB of data for a single entry 
which was  bascially help in storing large URLs
