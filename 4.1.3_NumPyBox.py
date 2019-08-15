#%%
import numpy as np

a = np.arange(3)
b = np.arange(-3,3).reshape((2,3))
c = np.arange(1,7).reshape((2,3))
d = np.arange(6).reshape((3,2))
e = np.linspace(-1,1,10)
print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)
print("e:",e)
#%%
print("a:",a.shape)
print("b:",b.shape)
print("c:",c.shape)
print("d:",d.shape)
print("e:",e.shape)

#%%
li = [[-3,-2,-1],
    [0,1,2]]
new = []
for i,j in enumerate(li):
    new.append([])
    for k in j:
        new[i].append(abs(k))
new
#%%
np.abs(b)

#%%
np.sin(e)

#%%
np.cos(e)

#%%
np.log(a)

#%%
np.log10(c)

#%%
np.exp(a)

#%%
a+10

#%%
a

#%%
b

#%%
a+b

#%%
a1 = a[:, np.newaxis]
a1

#%%
a+a1

#%%
c
#%%
np.mean(c)
#%%
c-np.mean(c)

#%%
b*2

#%%
b**3

#%%
b-a

#%%
a*b

#%%
a/c

#%%
c/a

#%%
c/(a+1e-6)

#%%
