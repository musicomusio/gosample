#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install janome')


# In[15]:


from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter,ExtractAttributeFilter


# In[ ]:





# In[143]:


txt = """"
後ろは楽ちんカットソー　ZIP付Vネックフレンチスリーブブラウス
部分はきれい目ジョーゼットで上品に。
背中は伸びる楽ちんカットソー！
異素材を前後で切り替えた優秀ブラウスが登場しました！！
胸元はスッキリ見えのVネック仕様にきらっと光るファスナーがポイントに。
広すぎず狭すぎず…キレイなネックラインにこだわりました。
すそ部分はタック入りで、落ち感が自然でキレイなニュアンスです。

上品な質感なのでオフィスでも着られるアイテムです。
休日の大人ブラウスコーデに！
オフィスのシンプルコーデに！
見た目はかっちり、着心地は楽ちんな大人女子のおすすめアイテムです♪♪

"""


# In[144]:


def chkword(v):
    if v.find('非自立') >= 0:
        return False
    elif v.find('接尾') >= 0:
        return False
    else:
        return True
wordlist = []
tokenizer = Tokenizer()
token_filters = [POSKeepFilter(['名詞'])]
analyzer = Analyzer([], tokenizer, token_filters)
for token in analyzer.analyze(txt):
    sym = chkword(token.part_of_speech)

    if (token.part_of_speech.find('一般') >= 0) and sym:
        #print(token)
        wordlist.append(token.surface)

import pandas as pd
sr = pd.DataFrame(wordlist,columns=['word'])


# In[145]:


sr['word'].unique()


# In[ ]:





# In[ ]:




