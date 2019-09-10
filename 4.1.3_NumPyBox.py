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
b

#%%
a

#%%
np.dot(b, a)

#%%
b @ a

#%%
a @ b

#%%
d

#%%
b @ d
#%%
d @ b


#%%
b

#%%
d

#%%
np.all(b > 0)

#%%
b > 0

#%%
b[b>0]

#%%
a

#%%
b

#%%
c
#%%
a == b

#%%
b[(b == c) | (a == b)]

#%%
np.allclose(b, c)

#%%
np.allclose(b, c, atol=10)


#%%
import pandas as pd

#%%
ser = pd.Series([10,20,30,40])
ser
#%%
df = pd.DataFrame([[10,"a", True],
            [20, "b", False],
            [30, "c", False],
            [40, "d", True]])

df

#%%
df.shape

#%%
df.dtypes

#%%
df = pd.DataFrame(np.arange(100).reshape((25, 4)))
df

#%%
df.shape

#%%
df = pd.DataFrame(np.arange(6).reshape((3, 2)))
df

#%%
df.index = ["01", "02", "03"]
df.columns = ["A", "B"]
df
#%%
named_df = pd.DataFrame(np.arange(6).reshape((3,2)),
                columns = ["A列", "B列"],
                index = ["１行目", "２行目", "３行目"])
named_df

#%%
import numpy as np
import pandas as pd
df=pd.DataFrame(np.arange(12).reshape(4, 3),
    columns=["A", "B", "C"],
    index=["1行目", "2行目", "3行目", "4行目"])

df

#%%
df["A"]

#%%
df[["A", "B"]]

#%%
df[:2]

#%%
df.loc[:, :]

#%%
df.loc[:, "A"]

#%%
df.loc[:, ["A", "B"]]

#%%
df.loc["1行目", :]

#%%
df.loc[["1行目", "3行目"], :]

#%%
df.loc[["1行目"], ["A", "C"]]

#%%
df.iloc[1, 1]

#%%
df.iloc[1:, 1]

#%%
df.iloc[:2, 2]

#%%
df.iloc[1:, :2]

#%%
