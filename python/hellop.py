#!/usr/bin/env python
# coding: utf-8

# In[7]:


from flask import Flask, escape, request 

app = Flask(__name__)

@app.route("/")

def hello():
        name = request.args.get("name", "World")
        return f'Hello, {escape(name)}!'
           
# if __name__ = "__main__":
#            app.run(debug = True)


# In[ ]:




