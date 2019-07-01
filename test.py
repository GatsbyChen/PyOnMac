# import tensorflow as tf
#
# #初始化一个Tensorflow的常量：Hello Google Tensorflow! 字符串，并命名为greeting作为一个计算模块
# greeting = tf.constant('Hello Google Tensorflow!')
# #启动一个会话
# sess = tf.Session()
# #使用会话执行greeting计算模块
# result = sess.run(greeting)
# print(result)
# sess.close()

from bs4 import BeautifulSoup as bsp
import requests

url = 'http://www.mdic.gov.br/index.php/comercio-exterior/defesa-comercial/140-investigacoes-em-curso/3669-etanolaminas-revisao'

r = requests.get(url)
demo = r.text

soup = bsp(demo, "html.parser")
table = soup.find(class_ = 'item-page').find_all('p')
for i in table:
    print(i)# 使用prettify()格式化显示输出