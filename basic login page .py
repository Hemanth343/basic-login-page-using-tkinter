#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from functools import partial


# In[2]:


def validateLogin(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
    return


# In[3]:


tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')


# In[4]:


#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)



# In[5]:


#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='@').grid(row=1, column=1)


# In[6]:


validateLogin = partial(validateLogin, username, password)


# In[ ]:


#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()


# In[ ]:





# In[ ]:




