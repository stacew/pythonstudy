from matplotlib import font_manager, rc
import platform
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

CCTV_seoul = pd.read_csv('외부API/file/CCTV_in_Seoul.csv', encoding='utf-8')

CCTV_seoul.head()
CCTV_seoul.columns

CCTV_seoul.rename(columns={CCTV_seoul.columns[0]: '구별'}, inplace=True)
CCTV_seoul.head()

pop_Seoul = pd.read_excel('외부API/file/POP_in_Seoul.xls', encoding='utf-8')
pop_Seoul.head()

pop_Seoul = pd.read_excel('외부API/file/POP_in_Seoul.xls',
                          header=2,
                          usecols='B, D, G, J, N',
                          encoding='utf-8')
pop_Seoul.head()

CCTV_seoul.sort_values(by='소계', ascending=True).head()

CCTV_seoul.sort_values(by='소계', ascending=False).head()
pop_Seoul.head(5)

pop_Seoul.rename(columns={pop_Seoul.columns[0]: '구별',
                          pop_Seoul.columns[1]: '인구수',
                          pop_Seoul.columns[2]: '한국인',
                          pop_Seoul.columns[3]: '외국인',
                          pop_Seoul.columns[4]: '고령자',
                          }, inplace=True)
pop_Seoul.head()

pop_Seoul.drop([0], inplace=True)
pop_Seoul.head()

pop_Seoul['구별'].unique()

pop_Seoul[pop_Seoul['구별'].isnull()]

pop_Seoul.drop([26], inplace=True)

pop_Seoul[pop_Seoul['구별'].isnull()]

pop_Seoul['외국인비율'] = pop_Seoul['외국인']/pop_Seoul['인구수']*100
pop_Seoul.head()

pop_Seoul['고령자비율'] = pop_Seoul['고령자']/pop_Seoul['인구수']*100
pop_Seoul.head()

pop_Seoul.sort_values(by='인구수', ascending=False).head(5)

pop_Seoul.sort_values(by='인구수', ascending=True).head(5)

pop_Seoul.sort_values(by='외국인비율', ascending=True).head(5)
pop_Seoul.sort_values(by='외국인비율', ascending=False).head(5)
pop_Seoul.sort_values(by='고령자비율', ascending=False).head(5)
CCTV_seoul['최근증가율'] = (CCTV_seoul['2016년'] +
                       CCTV_seoul['2015년'] +
                       CCTV_seoul['2014년']) / CCTV_seoul['2013년도 이전'] * 100
CCTV_seoul.head()

CCTV_seoul.sort_values(by='최근증가율', ascending=False).head(5)

data_result = pd.merge(CCTV_seoul, pop_Seoul, on='구별')
data_result.head()

del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']

data_result.head()

data_result.set_index('구별', inplace=True)

data_result.head()


np.corrcoef(data_result['고령자비율'], data_result['소계'])
np.corrcoef(data_result['외국인비율'], data_result['소계'])
np.corrcoef(data_result['인구수'], data_result['소계'])
data_result.sort_values(by='인구수', ascending=False).head()
np.corrcoef(data_result['최근증가율'], data_result['소계'])

# from IPython import get_ipython # 파이썬 3.7 이하 time.clock()지원 문제
#get_ipython().run_line_magic('matplotlib', 'inline')


plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')
data_result.head()

plt.figure()

data_result['소계'].plot(kind='barh', grid=True, figsize=(10, 10))

plt.show()

plt.figure()

data_result['소계'].sort_values().plot(kind='barh', grid=True, figsize=(10, 10))

plt.show()

data_result['CCTV비율'] = data_result['소계']/data_result['인구수'] * 100

plt.figure()

data_result['CCTV비율'].sort_values().plot(
    kind='barh', grid=True, figsize=(10, 10))

plt.show()

plt.figure(figsize=(6, 6))

plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.xlabel('인구수')
plt.ylabel('CCTV 소계')
plt.grid()

plt.show()
