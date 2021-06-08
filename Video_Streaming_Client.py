#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2, socket, pickle, os


# In[2]:


s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
serverip="192.168.43.54"
serverport=307


# In[31]:


cap = cv2.VideoCapture(0)
while True:
    ret,photo = cap.read()
    cv2.imshow('my pic', photo)
    ret, buffer = cv2.imencode(".jpg", photo, [int(cv2.IMWRITE_JPEG_QUALITY),30])
    x_as_bytes = pickle.dumps(buffer)
    s.sendto(x_as_bytes,(serverip , serverport))
    if cv2.waitKey(10) == 13:
        break
  
cv2.destroyAllWindows()
cap.release()


# In[ ]:




