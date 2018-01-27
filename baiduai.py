# -*- coding: utf-8 -*-
from aip import AipNlp
from config import APP_ID, API_KEY, SECRET_KEY
__author__ = 'sml'

text='进入币圈后，每天都过得很痛苦'
text2='通过类似与维基百科的协同编辑技术，意在对抗如今横行于社交网络和大型信息分发平台的虚假新闻和误导信息'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
client.depParser(text)