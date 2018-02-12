# CaesarCipher

## TASK 1A: Caesar Cipher

**Folder Name** : Python Task
**File Name** : caesar.py

**Description** : Utility to encrypt and decrypt message

**Command** : `python caesar.py encrypt hello`


## TASK 1B: Simple Web-Server

**Command to start server**

- To install node module run `npm install`
- To start node server `node server.js`


**Webservice end point**


**Encrypt message**
```curl -X GET \
  'http://localhost:5000/caesar/encrypt?message=hello' \
  -H 'Cache-Control: no-cache'
```

**Decrypt Message**

```
    curl -X GET \
    'http://localhost:5000/caesar/decrypt?message=EBIIL' \
    -H 'Cache-Control: no-cache'
```

## TASK 2: Find the Path && TASK 2 Bonus: Find the Path II

**Folder Name** : Python Task
**File Name** : path.py

**Description** : Connect neighbouring fields in this matrix to find exactly one path that sums up to 21.
Print the matrix and the values and coordinates of the path on the command line.
It will also print the shortest part

**Command to find path**

`python path.py`