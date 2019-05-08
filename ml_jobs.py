
# coding: utf-8

# In[5]:


import numpy as np
import json

# In[6]:


files = ["iris", "mnist", "cancer", "wine"]


# In[15]:
with open('ml_train_jobs.json', 'w') as f:
    id_num = 6000
    for i in range(300):
        line_item = {}
        line_item['ram'] = np.random.randint(1,5)
        line_item['id'] = 6000 + i
        line_item['type'] = 'ml'
        job_name = "python ml.py --dataset "
        job_name += files[np.random.randint(0, 4)]
        line_item['command'] = job_name
        line_item['cpu'] = np.random.randint(1,4)
        f.write(json.dumps(line_item) + '\n')
