# from sklearn.datasets import load_iris, fetch_20newsgroups, load_boston
import numpy as np

# news = fetch_20newsgroups(subset='all', data_home='data')
# print(news.feature_names)  #这个没有
# print(news.DESCR)
# print('-' * 50)
# print(news.data[0])
# print(news.target[0])
# print(len(news.data))
# print('-' * 50)
# print(news.target)
# print(min(news.target), max(news.target))
a = np.arange(4)
b = np.array([0,1,2,6])
print(a[(a==b)])
print(len(a[(a!=b)]))