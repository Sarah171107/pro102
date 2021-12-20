import cv2 
import dropbox
import time
import random
starttime=time.time()
def takesnapshot ():
    number=random.randint(0,100)
    videocaptureobject = cv2. VideoCapture(0)
    result = True
    while (result): 
        ret,frame= videocaptureobject.read()
        imagename='img'+str(number)+'.png'
        cv2.imwrite(imagename,frame)
        starttime=time.time
        result= False
    return imagename
    print('snapshottaken')
    videocaptureobject.release()
    cv2.destroyAllWindows()
def uploadfile(imagename):
    accesstoken='AoYx-0CPgVcAAAAAAAAAAQOTM02amoUK0NJjzfkAhinb4jTvsaXSxMipCr3xlUl8'
    file=imagename
    filefrom=file
    fileto='Dropbox/New folder'
    dbx=dropbox.Dropbox(accesstoken)
    
    
    with open(filefrom,'rb')as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print('fileuploaded')

def main ():
    while(True):
        if((time.time()-starttime)>=5):
            name=takesnapshot()
            uploadfile(name)
main()                        