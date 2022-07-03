from types import TracebackType
import Encryption,Constant,getpass
from firebase import firebase
from datetime import date,datetime
from uuid import getnode
FirebaseDatabase = firebase.FirebaseApplication(Constant.DB_PATH,None)

def getMac():
    return getnode()
def setPassword(p):
    return Encryption.encrypt(p)
def getPassword(p):
    return Encryption.decrypt(p)
def getNowDate():
    return date.today().strftime(Constant.TODAY)
def getdateAndHour():
    return datetime.now().strftime(Constant.YEARHOUR)
def pullUserCollection(collectionPath):
    try:
        response = FirebaseDatabase.get(collectionPath,None)
        return response
    except Exception:
        print(Exception.__name__)
def pullProfileCodes(username,password):
    try:
        response = FirebaseDatabase.get(Constant.DB_PATH_RECORDS,None)
        keyList=[]
        itemList=[]
        for key in response:
            keyList.append(key)
        for item in range(len(response)):
            itemList.append({
                Constant.DB_GET_USERNAME:response[keyList[item]][Constant.DB_VALUES_RECORD_USERNAME],
                Constant.DB_GET_PASSWORD:response[keyList[item]][Constant.DB_VALUES_RECORD_PASSWORD],
                Constant.DB_GET_PROFILECODE:response[keyList[item]][Constant.DB_VALUES_RECORD_PROFILECODES]
            })
        profileCode=""
        for iterator in range(len(itemList)):
            if(itemList[iterator][Constant.DB_GET_USERNAME]==username and Encryption.decrypt(itemList[iterator][Constant.DB_GET_PASSWORD]) == password):
                profileCode=itemList[iterator][Constant.DB_GET_PROFILECODE]     
        return profileCode
    except Exception:
        print(Exception.__name__)
def postProfileCodes(data):
    try:
        print(data)
        response=FirebaseDatabase.post(Constant.DB_PATH_RECORDS,data)
        return response
    except Exception:
        print(Exception.__name__)
def pullProfileCodesName(profileCodes):
    response=FirebaseDatabase.get(Constant.DB_PATH_PROFILECODES,None)
    keyList=[]
    for key in response:
        keyList.append(key)
    for j in range(len(response)):
        if(list(response[keyList[j]].keys())[0]==profileCodes):
            return response[keyList[j]][profileCodes]
def pullAuthorization(profileCode):
        response=FirebaseDatabase.get(Constant.DB_PATH_AUTHORIZATION,None)
        keyList=[]
        for key in response:
            keyList.append(key)
        for item in range(len(response)):
            if(list(response[keyList[item]].keys())[0]==profileCode):           
                return response[keyList[item]][profileCode]
def authcheck(reqList,inputList):
    keyList=[]
    resList=[]
    find=False
    for key in reqList:
        keyList.append(key)
    for item in range(len(reqList)):
        resList.append(reqList[keyList[item]])
    for iterator in range(len(resList)):
        if(resList[iterator][Constant.DB_VALUES_RECORD_USERNAME]==inputList["LOCAL_INPUT_USERNAME"] and  Encryption.decrypt(resList[iterator][Constant.DB_VALUES_RECORD_PASSWORD])==inputList["LOCAL_INPUT_PASSWORD"]):
            find=True
            break
    if(find is True):
        return True
    else:
        return False
def inputIsValid(n,p):
    n=n.strip()
    p=p.strip()
    if(
        n != ""     and 
        n != None   and  
        p != ""     and  
        p != None   and  
        len(n) != 0 and  
        len(p) != 0 and
        len(n) >  3 and
        len(p) >  3
    ):
        return True
    else:
        return False
def pullAuthenticationData(INPUT_USERNAME,INPUT_PASSWORD):
    resList=[]
    inList=[]
    if(inputIsValid(INPUT_USERNAME,INPUT_PASSWORD) is True):
        userList=pullUserCollection(Constant.DB_PATH_RECORDS)
        inList={
            "LOCAL_INPUT_USERNAME":INPUT_USERNAME,
            "LOCAL_INPUT_PASSWORD":INPUT_PASSWORD
        }
        if(authcheck(userList,inList) is True):
            resList.append({"usrn":INPUT_USERNAME,"passw":INPUT_PASSWORD})
            resList.append({"find":True})
        else:
            resList.append({"find":False})
        return resList
    else:
        return resList