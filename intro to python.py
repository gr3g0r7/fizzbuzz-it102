
# coding: utf-8

# In[25]:


for i in range (1,51):
    print(i,end=' ')
    print( )
    if i % 3 == 0:
        print("fizz")
        
    elif (i % 5 == 0):
        print ("fizzbuzz")
        
    else: 
        if i % 5 == 0:
            print("buzz")
            print( )

