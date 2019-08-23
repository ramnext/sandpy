#%%
print('Hello conda')

#%%
import datetime

print(datetime.date.today())

#%%
%timeit -n 1000 -r 10 [x*x for x in range(10000)]

#%%
%%timeit -n 1000 -r 10

# 0から9999の2乗リストを生成（forループ）
# ループ回数: 1000回、試行回数： 10回
ret = []
for x in range(10000):
    ret.append(x*x)

#%%
for year in [1950,2000,2020]:
    if year < 1989:
        print('昭和')
    elif year < 2019:
        print('平成')
    else:
        print('新元号')

#%%
try:
    1/0
except ZeroDivisionError as zd:
    print('0で割れません')

#%%
names = ['spam', 'ham', 'eggs']

lens = []

for name in names:
    lens.append(len(name))

#%%
lens

#%%
[len(name) for name in names]

#%%
{len(name) for name in names}

#%%
{name: len(name) for name in names}

#%%
[x*x for x in range(10) if x % 2 == 0]

#%%
[[(y, x*x) for x in range(10) if x % 2 == 0] for y in range(3)]

#%%
l = [x*x for x in range(100000)]

type(l), len(l)

#%%
g = (x*x for x in range(100000))

type(g)

#%%
next(g), next(g), next(g)

#%%
with open('sample.txt', 'w', encoding='utf-8') as f:
    f.write('こんにちは¥n')
    f.write('Python.¥n')

#%%
f.closed

#%%
with open('sample.txt', 'r', encoding='utf-8') as f:
    data = f.read()

data

#%%
s1 = 'hello python.'

#%%
s1.upper(), s1.lower(), s1.title()

#%%
s1.replace('hello', 'Hi')

#%%
s2 = ' spam ham  eggs  '

#%%
s2.split()

#%%
s2.strip()

#%%
s3 = 'sample.jpg'

#%%
s3.endswith(('jpg', 'gif', 'png'))

#%%
'1234567890'.isdigit()

#%%
len(s1)

#%%
'py' in s1

#%%
'-'.join(['spam', 'ham', 'eggs'])

#%%
lang, num, name = 'python', 10, 'takanory'

#%%
'{}は{}が好きです'.format(name, lang)

#%%
'{1}は{0}が好きです'.format(lang, name)

#%%
'{n}は{num}の{num}乗 {l}が好きです'.format(l=lang, n=name, num=num)

#%%
import re

#%%
prog = re.compile('(P(yth|l)|Z)o[pn]e?')

#%%
prog.search('Python')

#%%
prog.search('Spam')

#%%
from datetime import datetime, date

#%%
datetime.now()

#%%
date.today()

#%%
date.today() - date(2008, 12, 3)

#%%
datetime.now().isoformat()

#%%
date.today().strftime('%Y年%m月%d日')

#%%
datetime.strptime('2019年7月11日', '%Y年%m月%d日')

#%%
import pickle

#%%
d = {'today': date.today(), 'delta': date(2020, 1, 1)-date.today()}

#%%
d

#%%
pickle.dumps(d)

#%%
with open('date.pkl', 'wb') as f:
    pickle.dump(d, f)

#%%
with open('date.pkl', 'rb') as f:
    new_d = pickle.load(f)

#%%
new_d

#%%
import numpy as np

#%%
np.array([1,2,np.nan])

#%%
np.linspace(0,1,5)

#%%
l = np.array([2,2,6,1,3])
np.diff(l)

#%%
a = np.array([1,5,4])

#%%
a1 = a

#%%
f = np.random.random((3,2))
f

#%%
np.random.seed(123)
np.random.random((3,2))

#%%
np.random.seed(123)
np.random.rand(1,10)

#%%
np.pi

#%%
print(a)
print(a1)

#%%
np.concatenate([a, a1])

#%%
b = np.array([[1,2,3],[4,5,6]])

#%%
b

#%%
b.shape

#%%
c1 = np.array([0,1,2,3,4,5])
c1

#%%
c2 = c1.reshape((2,3))

#%%
c2

#%%
c3 = c2.ravel()
c3

#%%
c4 = c2.flatten()

#%%
c4

#%%
a.dtype

#%%
b

#%%
b1 = np.array([[10],[20]])
b1

#%%
np.concatenate([b,b1],axis=1)

#%%
b[:,2] = 8
b

#%%
np.hstack([b,b1])

#%%
b2 = np.array([30,60,45])
b2

#%%
b3 = np.vstack([b,b2])
b3

#%%
first, second = np.hsplit(b3,[2])

#%%
first

#%%
second

#%%
first1, second1 = np.vsplit(b3,[2])

#%%
first1

#%%
second1

#%%
b.T

#%%
a[np.newaxis,:]

#%%
a[:,np.newaxis]

#%%
m = np.arange(0,4)
m

#%%
n = np.arange(4,7)
n

#%%
xx, yy = np.meshgrid(m,n)
xx

#%%
yy

#%%
