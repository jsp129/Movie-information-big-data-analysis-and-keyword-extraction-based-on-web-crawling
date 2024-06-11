#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup   ### 필요한 패키지 로드
import urllib.request as req
import math
import pandas as pd
from konlpy.tag import Okt 
from collections import Counter
import matplotlib as mpl
import matplotlib.pyplot as plt
import nltk
import matplotlib.font_manager as fm
import konlpy.tag
import os
import re
from collections import Counter
import numpy as np
from ast import literal_eval
import re


# In[3]:


movies_pd = pd.read_csv('C:\\Users\\user\\Documents\\movie_data2.csv')
movies_pd.columns = ['movie_id', 'title', 'star', 'movie_rating', 'genre', 'director', 'actors', 'summary']
print(movies_pd)



# In[ ]:


with open('C:/Users/user/Documents/Movie_123519.txt', 'r') as f:
    content1 = f.read()
with open('C:/Users/user/Documents/Movie_125494.txt', 'r') as f:
    content2 = f.read()  
with open('C:/Users/user/Documents/Movie_134963.txt', 'r') as f:
    content3 = f.read()
with open('C:/Users/user/Documents/Movie_136898.txt', 'r') as f:
    content4 = f.read()    
with open('C:/Users/user/Documents/Movie_137008.txt', 'r') as f:
    content5 = f.read()        
with open('C:/Users/user/Documents/Movie_137326.txt', 'r') as f:
    content6 = f.read()    
with open('C:/Users/user/Documents/Movie_144379.txt', 'r') as f:
    content7 = f.read()    
with open('C:/Users/user/Documents/Movie_151728.txt', 'r') as f:
    content8 = f.read()    
with open('C:/Users/user/Documents/Movie_153620.txt', 'r') as f:
    content9 = f.read()    
with open('C:/Users/user/Documents/Movie_154449.txt', 'r') as f:
    content10 = f.read()    
with open('C:/Users/user/Documents/Movie_154598.txt', 'r') as f:
    content11 = f.read()    
with open('C:/Users/user/Documents/Movie_158626.txt', 'r') as f:
    content12 = f.read()    
with open('C:/Users/user/Documents/Movie_158885.txt', 'r') as f:
    content13 = f.read() 
with open('C:/Users/user/Documents/Movie_165026.txt', 'r') as f:
    content15 = f.read()     
with open('C:/Users/user/Documents/Movie_168298.txt', 'r') as f:
    content16 = f.read()     
with open('C:/Users/user/Documents/Movie_172454.txt', 'r') as f:
    content17 = f.read()     
with open('C:/Users/user/Documents/Movie_184571.txt', 'r') as f:
    content18 = f.read()    
with open('C:/Users/user/Documents/Movie_203097.txt', 'r') as f:
    content19 = f.read()    
with open('C:/Users/user/Documents/Movie_85578.txt', 'r') as f:
    content20 = f.read() 
with open('C:/Users/user/Documents/Movie_85579.txt', 'r') as f:
    content21 = f.read() 
with open('C:/Users/user/Documents/Movie_99354.txt', 'r') as f:
    content22 = f.read() 


regex = re.compile('{}(.*){}'.format(re.escape('########'), re.escape(':')))
text1 = regex.findall(content1)
text2 = regex.findall(content2)
text3 = regex.findall(content3)
text4 = regex.findall(content4)
text5 = regex.findall(content5)
text6 = regex.findall(content6)
text7 = regex.findall(content7)
text8 = regex.findall(content8)
text9 = regex.findall(content9)
text10 = regex.findall(content10)
text11 = regex.findall(content11)
text12 = regex.findall(content12)
text13 = regex.findall(content13)
text15 = regex.findall(content15)
text16 = regex.findall(content16)
text17 = regex.findall(content17)
text18 = regex.findall(content18)
text19 = regex.findall(content19)
text20 = regex.findall(content20)
text21 = regex.findall(content21)
text22 = regex.findall(content22)

filtered_content1 = content1.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content2 = content2.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content3 = content3.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content4 = content4.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content5 = content5.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content6 = content6.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content7 = content7.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content8 = content8.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content9 = content9.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content10 = content10.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content11 = content11.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content12 = content12.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content13 = content13.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content15 = content15.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content16 = content16.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content17 = content17.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content18 = content18.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content19 = content19.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content20 = content20.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content21 = content21.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
filtered_content22 = content22.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')

Okt = konlpy.tag.Okt()
Okt_morphs1 = Okt.pos(filtered_content1)  # 튜플반환
Okt_morphs2 = Okt.pos(filtered_content2)
Okt_morphs3 = Okt.pos(filtered_content3)
Okt_morphs4 = Okt.pos(filtered_content4)
Okt_morphs5 = Okt.pos(filtered_content5)
Okt_morphs6 = Okt.pos(filtered_content6)
Okt_morphs7 = Okt.pos(filtered_content7)
Okt_morphs8 = Okt.pos(filtered_content8)
Okt_morphs9 = Okt.pos(filtered_content9)
Okt_morphs10 = Okt.pos(filtered_content10)
Okt_morphs11 = Okt.pos(filtered_content11)
Okt_morphs12 = Okt.pos(filtered_content12)
Okt_morphs13 = Okt.pos(filtered_content13)
Okt_morphs15 = Okt.pos(filtered_content15)
Okt_morphs16 = Okt.pos(filtered_content16)
Okt_morphs17 = Okt.pos(filtered_content17)
Okt_morphs18 = Okt.pos(filtered_content18)
Okt_morphs19 = Okt.pos(filtered_content19)
Okt_morphs20 = Okt.pos(filtered_content20)
Okt_morphs21 = Okt.pos(filtered_content21)
Okt_morphs22 = Okt.pos(filtered_content22)

Noun_words1 = []
for word, pos in Okt_morphs1:
    if pos == 'Noun':
        Noun_words1.append(word)
Noun_words2 = []
for word, pos in Okt_morphs2:
    if pos == 'Noun':
        Noun_words2.append(word)
Noun_words3 = []
for word, pos in Okt_morphs3:
    if pos == 'Noun':
        Noun_words3.append(word)
Noun_words4 = []
for word, pos in Okt_morphs4:
    if pos == 'Noun':
        Noun_words4.append(word)
Noun_words5 = []
for word, pos in Okt_morphs5:
    if pos == 'Noun':
        Noun_words5.append(word)
Noun_words6 = []
for word, pos in Okt_morphs6:
    if pos == 'Noun':
        Noun_words6.append(word)
Noun_words7 = []
for word, pos in Okt_morphs7:
    if pos == 'Noun':
        Noun_words7.append(word)
Noun_words8 = []
for word, pos in Okt_morphs8:
    if pos == 'Noun':
        Noun_words8.append(word)
Noun_words9 = []
for word, pos in Okt_morphs9:
    if pos == 'Noun':
        Noun_words9.append(word)
Noun_words10 = []
for word, pos in Okt_morphs10:
    if pos == 'Noun':
        Noun_words10.append(word)
Noun_words11 = []
for word, pos in Okt_morphs11:
    if pos == 'Noun':
        Noun_words11.append(word)
Noun_words12 = []
for word, pos in Okt_morphs12:
    if pos == 'Noun':
        Noun_words12.append(word)
Noun_words13 = []
for word, pos in Okt_morphs13:
    if pos == 'Noun':
        Noun_words13.append(word)
Noun_words15 = []
for word, pos in Okt_morphs15:
    if pos == 'Noun':
        Noun_words15.append(word)
Noun_words16 = []
for word, pos in Okt_morphs16:
    if pos == 'Noun':
        Noun_words16.append(word)
Noun_words17 = []
for word, pos in Okt_morphs17:
    if pos == 'Noun':
        Noun_words17.append(word)
Noun_words18 = []
for word, pos in Okt_morphs18:
    if pos == 'Noun':
        Noun_words18.append(word)
Noun_words19 = []
for word, pos in Okt_morphs19:
    if pos == 'Noun':
        Noun_words19.append(word)
Noun_words20 = []
for word, pos in Okt_morphs20:
    if pos == 'Noun':
        Noun_words20.append(word)
Noun_words21 = []
for word, pos in Okt_morphs21:
    if pos == 'Noun':
        Noun_words21.append(word)
Noun_words22 = []
for word, pos in Okt_morphs22:
    if pos == 'Noun':
        Noun_words22.append(word)
        
        
stopwords = '{', '}', '[', ']', '\’', '?', '!', 'ㄴ', 'ㄹ','\"', ')', '(', '...', '\'','은', '는', '이', '가', ',', '.','개연','편이','백인호','남자','눈','이건','보지','임','자지','개','여자','흑인','별로','김고은','밤','팬','이치','빨갱이','선배','치인트','곤지암','캐스팅','걸','모양','퍼시픽림','하정우','아가씨','가슴','상미','손예진','김희애','김민희', '박찬욱','홍설','박해진','중','김태리', '장면','중국','편', '자본', '이영화','쓰레기','스필버그', '스티븐', '역시','김수현', '설리' ,'뭐' ,'블랙', '팬서', '와칸','코코', '오연서', '유정' ,'율','클레멘타인','싱크로','건담', '드라마','김태리','그레이', '장면' ,'엘리' ,'김강우' ,'김상경', '선예진' ,'소지섭', '공포영화', '한국' ,'소리' ,'사마' ,'위해','하이바라' ,'슈','일베충', '선동' ,'일베' ,'오유','쿠키','돈','이해','꼭','영상','재미','더','그냥','포함','마지막', '아', '휴','연기','평점','사람','점','보고','정말','카이','더빙','볼','워','책','내용','스토리','액션','보기','감독','처음','말','정도','거','은','는','연기력','생각','픽사','보이지','자체','바다','코난','수','다시','디즈니','스포일러','목적','진짜','원작','배우','장동건','류승룡','감상','평','내','영화','극장판','관람객','코난', '아이구', '아이쿠', '아이고', '어', '나', '우리', '저희', '따라', '의해','을', '를', '에', '의', '가', '으로', '로', '에게', '뿐이다', '의거하여', '근거하여', '입각하여', '기준으로', '예하면', '예를 들면','예를 들자면', '저', '소인', '소생', '저희', '지말고', '하지마', '하지마라', '다른', '물론', '또한', '그리고', '비길수 없다', '해서는 안된다', '뿐만 아니라', '만이 아니다', '만은 아니다', '막론하고', '관계없이', '그치지 않다', '그러나', '그런데', '하지만','든간에', '논하지 않다', '따지지 않다', '설사', '비록', '더라도', '아니면', '만 못하다', '하는 편이 낫다', '불문하고', '향하여','향해서', '향하다', '쪽으로', '틈타', '이용하여', '타다', '오르다', '제외하고', '이 외에', '이 밖에', '하여야', '비로소', '한다면 몰라도', '외에도', '이곳', '여기', '부터', '기점으로', '따라서', '할 생각이다', '하려고하다', '이리하여', '그리하여','그렇게 함으로써', '하지만', '일때', '할때', '앞에서', '중에서', '보는데서', '으로써', '로써', '까지', '해야한다', '일것이다', '반드시', '할줄알다', '할수있다', '할수있어', '임에 틀림없다', '한다면', '등', '등등', '제', '겨우', '단지', '다만', '할뿐', '딩동','댕그', '대해서', '대하여', '대하면', '훨씬', '얼마나', '얼마만큼', '얼마큼', '남짓', '여', '얼마간', '약간', '다소', '좀', '조금','다수', '몇', '얼마', '지만', '하물며', '또한', '그러나', '그렇지만', '하지만', '이외에도', '대해 말하자면', '뿐이다', '다음에','반대로', '반대로 말하자면', '이와 반대로', '바꾸어서 말하면', '바꾸어서 한다면', '만약', '그렇지않으면', '까악', '툭', '딱','삐걱거리다', '보드득', '비걱거리다', '꽈당', '응당', '해야한다', '에 가서', '각', '각각', '여러분', '각종', '각자', '제각기','하도록하다', '와', '과', '그러므로', '그래서', '고로', '한 까닭에', '하기 때문에', '거니와', '이지만', '대하여', '관하여', '관한','과연', '실로', '아니나다를가', '생각한대로', '진짜로', '한적이있다', '하곤하였다', '하', '하하', '허허', '아하', '거바', '와', '오','왜', '어째서', '무엇때문에', '어찌', '하겠는가', '무슨', '어디', '어느곳', '더군다나', '하물며', '더욱이는', '어느때', '언제', '야','이봐', '어이', '여보시오', '흐흐', '흥', '휴', '헉헉', '헐떡헐떡', '영차', '여차', '어기여차', '끙끙', '아야', '앗', '아야','콸콸','졸졸', '좍좍', '뚝뚝', '주룩주룩', '솨', '우르르', '그래도', '또', '그리고', '바꾸어말하면', '바꾸어말하자면', '혹은', '혹시', '답다', '및', '그에 따르는', '때가 되어', '즉', '지든지', '설령', '가령', '하더라도', '할지라도', '일지라도', '지든지', '몇', '거의','하마터면', '인젠', '이젠', '된바에야', '된이상', '만큼\t어찌됏든', '그위에', '게다가', '점에서 보아', '비추어 보아', '고려하면','하게될것이다', '일것이다', '비교적', '좀', '보다더', '비하면', '시키다', '하게하다', '할만하다', '의해서', '연이서', '이어서','잇따라', '뒤따라', '뒤이어', '결국', '의지하여', '기대여', '통하여', '자마자', '더욱더', '불구하고', '얼마든지', '마음대로','주저하지 않고', '곧', '즉시', '바로', '당장', '하자마자', '밖에 안된다', '하면된다', '그래', '그렇지', '요컨대', '다시 말하자면','바꿔 말하면', '즉', '구체적으로', '말하자면', '시작하여', '시초에', '이상', '허', '헉', '허걱', '바와같이', '해도좋다', '해도된다','게다가', '더구나', '하물며', '와르르', '팍', '퍽', '펄렁', '동안', '이래', '하고있었다', '이었다', '에서', '로부터', '까지', '예하면','했어요', '해요', '함께', '같이', '더불어', '마저', '마저도', '양자', '모두', '습니다', '가까스로', '하려고하다', '즈음하여', '다른','다른 방면으로', '해봐요', '습니까', '했어요', '말할것도 없고', '무릎쓰고', '개의치않고', '하는것만 못하다', '하는것이 낫다','매','매번', '들', '모', '어느것', '어느', '로써', '갖고말하자면', '어디', '어느쪽', '어느것', '어느해', '어느 년도', '라 해도', '언젠가','어떤것', '어느것', '저기', '저쪽', '저것', '그때', '그럼', '그러면', '요만한걸', '그래', '그때', '저것만큼', '그저', '이르기까지','할 줄 안다', '할 힘이 있다', '너', '너희', '당신', '어찌', '설마', '차라리', '할지언정', '할지라도', '할망정', '할지언정', '구토하다','게우다', '토하다', '메쓰겁다', '옆사람', '퉤', '쳇', '의거하여', '근거하여', '의해', '따라', '힘입어', '그', '다음', '버금', '두번째로', '기타', '첫번째로', '나머지는', '그중에서', '견지에서', '형식으로 쓰여', '입장에서', '위해서', '단지', '의해되다', '하도록시키다', '뿐만아니라', '반대로', '전후', '전자', '앞의것', '잠시', '잠깐', '하면서', '그렇지만', '다음에', '그러한즉','그런즉', '남들', '아무거나', '어찌하든지', '같다', '비슷하다', '예컨대', '이럴정도로', '어떻게', '만약', '만일', '위에서 서술한바와같이', '인 듯하다', '하지 않는다면', '만약에', '무엇', '무슨', '어느', '어떤', '아래윗', '조차', '한데','그럼에도 불구하고', '여전히', '심지어', '까지도', '조차도', '하지 않도록', '않기 위하여', '때', '시각', '무렵', '시간', '동안','어때','어떠한', '하여금', '네', '예', '우선', '누구', '누가 알겠는가', '아무도', '줄은모른다', '줄은 몰랏다', '하는 김에', '겸사겸사', '하는바', '그런 까닭에', '한 이유는', '그러니', '그러니까', '때문에', '그', '너희', '그들', '너희들', '타인', '것', '것들','너', '위하여', '공동으로', '동시에', '하기 위하여', '어찌하여', '무엇때문에', '붕붕', '윙윙', '나', '우리', '엉엉', '휘익','윙윙', '오호', '아하', '어쨋든', '만 못하다\t하기보다는', '차라리', '하는 편이 낫다', '흐흐', '놀라다', '상대적으로 말하자면','마치', '아니라면', '쉿', '그렇지 않으면', '그렇지 않다면', '안 그러면', '아니었다면', '하든지', '아니면', '이라면', '좋아', '알았어','하는것도', '그만이다', '어쩔수 없다', '하나', '일', '일반적으로', '일단', '한켠으로는', '오자마자', '이렇게되면', '이와같다면','전부','한마디', '한항목', '근거로', '하기에', '아울러', '하지 않도록', '않기 위해서', '이르기까지', '이 되다', '로 인하여','까닭으로', '이유만으로', '이로 인하여', '그래서', '이 때문에', '그러므로', '그런 까닭에', '알 수 있다', '결론을 낼 수 있다', '으로 인하여', '있다', '어떤것', '관계가 있다', '관련이 있다', '연관되다', '어떤것들', '에 대해', '이리하여', '그리하여', '여부', '하기보다는', '하느니', '하면 할수록', '운운', '이러이러하다', '하구나', '하도다', '다시말하면', '다음으로', '에 있다', '에 달려 있다','우리', '우리들', '오히려', '하기는한데', '어떻게', '어떻해', '어찌됏어', '어때', '어째서', '본대로', '자', '이', '이쪽', '여기', '이것', '이번', '이렇게말하자면', '이런', '이러한', '이와 같은', '요만큼', '요만한 것', '얼마 안 되는 것', '이만큼', '이 정도의','이렇게 많은 것', '이와 같다', '이때', '이렇구나', '것과 같이', '끼익', '삐걱', '따위', '와 같은 사람들', '부류의 사람들', '왜냐하면','중의하나', '오직', '오로지', '에 한하다', '하기만 하면', '도착하다', '까지 미치다', '도달하다', '정도에 이르다', '할 지경이다','결과에 이르다', '관해서는', '여러분', '하고 있다', '한 후', '혼자', '자기', '자기집', '자신', '우에 종합한것과같이', '총적으로 보면','총적으로 말하면', '총적으로', '대로 하다', '으로서', '참', '그만이다', '할 따름이다', '쿵', '탕탕', '쾅쾅', '둥둥', '봐', '봐라','아이야', '아니', '와아', '응', '아이', '참나', '년', '월', '일', '령', '영', '일', '이', '삼', '사', '오', '육', '륙', '칠', '팔','구', '이천육', '이천칠', '이천팔', '이천구', '하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉', '령', '영', ' ㄴ다','이','가','우','구','추','끝','부','안','중간','뭘','캐릭터','알바'
unique_Noun_words1 = set(Noun_words1)
for word in unique_Noun_words1:
    if word in stopwords:
        while word in Noun_words1: Noun_words1.remove(word)  # 최종결과 : Noun_words
unique_Noun_words2 = set(Noun_words2)
for word in unique_Noun_words2:
    if word in stopwords:
        while word in Noun_words2: Noun_words2.remove(word)  # 최종결과 : Noun_words
unique_Noun_words3 = set(Noun_words3)
for word in unique_Noun_words3:
    if word in stopwords:
        while word in Noun_words3: Noun_words3.remove(word)  # 최종결과 : Noun_words
unique_Noun_words4 = set(Noun_words4)
for word in unique_Noun_words4:
    if word in stopwords:
        while word in Noun_words4: Noun_words4.remove(word)  # 최종결과 : Noun_words
unique_Noun_words5 = set(Noun_words5)
for word in unique_Noun_words5:
    if word in stopwords:
        while word in Noun_words5: Noun_words5.remove(word)  # 최종결과 : Noun_words
unique_Noun_words6 = set(Noun_words6)
for word in unique_Noun_words6:
    if word in stopwords:
        while word in Noun_words6: Noun_words6.remove(word)  # 최종결과 : Noun_words
unique_Noun_words7 = set(Noun_words7)
for word in unique_Noun_words7:
    if word in stopwords:
        while word in Noun_words7: Noun_words7.remove(word)  # 최종결과 : Noun_words
unique_Noun_words8 = set(Noun_words8)
for word in unique_Noun_words8:
    if word in stopwords:
        while word in Noun_words8: Noun_words8.remove(word)  # 최종결과 : Noun_words
unique_Noun_words9 = set(Noun_words9)
for word in unique_Noun_words9:
    if word in stopwords:
        while word in Noun_words9: Noun_words9.remove(word)  # 최종결과 : Noun_words
unique_Noun_words10 = set(Noun_words10)
for word in unique_Noun_words10:
    if word in stopwords:
        while word in Noun_words10: Noun_words10.remove(word)  # 최종결과 : Noun_words
unique_Noun_words11 = set(Noun_words11)
for word in unique_Noun_words11:
    if word in stopwords:
        while word in Noun_words11: Noun_words11.remove(word)  # 최종결과 : Noun_words
unique_Noun_words12 = set(Noun_words12)
for word in unique_Noun_words12:
    if word in stopwords:
        while word in Noun_words12: Noun_words12.remove(word)  # 최종결과 : Noun_words
unique_Noun_words13 = set(Noun_words13)
for word in unique_Noun_words13:
    if word in stopwords:
        while word in Noun_words13: Noun_words13.remove(word)  # 최종결과 : Noun_words
unique_Noun_words15 = set(Noun_words15)
for word in unique_Noun_words15:
    if word in stopwords:
        while word in Noun_words15: Noun_words15.remove(word)  # 최종결과 : Noun_words
unique_Noun_words16 = set(Noun_words16)
for word in unique_Noun_words16:
    if word in stopwords:
        while word in Noun_words16: Noun_words16.remove(word)  # 최종결과 : Noun_words
unique_Noun_words17 = set(Noun_words17)
for word in unique_Noun_words17:
    if word in stopwords:
        while word in Noun_words17: Noun_words17.remove(word)  # 최종결과 : Noun_words
unique_Noun_words18 = set(Noun_words18)
for word in unique_Noun_words18:
    if word in stopwords:
        while word in Noun_words18: Noun_words18.remove(word)  # 최종결과 : Noun_words
unique_Noun_words19 = set(Noun_words19)
for word in unique_Noun_words19:
    if word in stopwords:
        while word in Noun_words19: Noun_words19.remove(word)  # 최종결과 : Noun_words
unique_Noun_words20 = set(Noun_words20)
for word in unique_Noun_words20:
    if word in stopwords:
        while word in Noun_words20: Noun_words20.remove(word)  # 최종결과 : Noun_words
unique_Noun_words21 = set(Noun_words21)
for word in unique_Noun_words21:
    if word in stopwords:
        while word in Noun_words21: Noun_words21.remove(word)  # 최종결과 : Noun_words
unique_Noun_words22 = set(Noun_words22)
for word in unique_Noun_words22:
    if word in stopwords:
        while word in Noun_words22: Noun_words22.remove(word)  # 최종결과 : Noun_words
            
from collections import Counter
c1 = Counter(Noun_words1)
c2 = Counter(Noun_words2)
c3 = Counter(Noun_words3)
c4 = Counter(Noun_words4)
c5 = Counter(Noun_words5)
c6 = Counter(Noun_words6)
c7 = Counter(Noun_words7)
c8 = Counter(Noun_words8)
c9 = Counter(Noun_words9)
c10 = Counter(Noun_words10)
c11 = Counter(Noun_words11)
c12 = Counter(Noun_words12)
c13 = Counter(Noun_words13)
c15 = Counter(Noun_words15)
c16 = Counter(Noun_words16)
c17 = Counter(Noun_words17)
c18 = Counter(Noun_words18)
c19 = Counter(Noun_words19)
c20 = Counter(Noun_words20)
c21 = Counter(Noun_words21)
c22 = Counter(Noun_words22)

ck1 = c1.most_common(5)
ck2 = c2.most_common(5)
ck3 = c3.most_common(5)
ck4 = c4.most_common(5)
ck5 = c5.most_common(5)
ck6 = c6.most_common(5)
ck7 = c7.most_common(5)
ck8 = c8.most_common(5)
ck9 = c9.most_common(5)
ck10 = c10.most_common(5)
ck11 = c11.most_common(5)
ck12 = c12.most_common(5)
ck13 = c13.most_common(5)
ck15 = c15.most_common(5)
ck16 = c16.most_common(5)
ck17 = c17.most_common(5)
ck18 = c18.most_common(5)
ck19 = c19.most_common(5)
ck20 = c20.most_common(5)
ck21 = c21.most_common(5)
ck22 = c22.most_common(5)

ck1_1 = [(text1[0], ck1[0][0], ck1[1][0], ck1[2][0], ck1[3][0], ck1[4][0])]
ck2_2 = [(text2[0], ck2[0][0], ck2[1][0], ck2[2][0], ck2[3][0], ck2[4][0])]
ck3_3 = [(text3[0], ck3[0][0], ck3[1][0], ck3[2][0], ck3[3][0], ck3[4][0])]
ck4_4 = [(text4[0], ck4[0][0], ck4[1][0], ck4[2][0], ck4[3][0], ck4[4][0])]
ck5_5 = [(text5[0], ck5[0][0], ck5[1][0], ck5[2][0], ck5[3][0], ck5[4][0])]
ck6_6 = [(text6[0], ck6[0][0], ck6[1][0], ck6[2][0], ck6[3][0], ck6[4][0])]
ck7_7 = [(text7[0], ck7[0][0], ck7[1][0], ck7[2][0], ck7[3][0], ck7[4][0])]
ck8_8 = [(text8[0], ck8[0][0], ck8[1][0], ck8[2][0], ck8[3][0], ck8[4][0])]
ck9_9 = [(text9[0], ck9[0][0], ck9[1][0], ck9[2][0], ck9[3][0], ck9[4][0])]
ck10_10 = [(text10[0], ck10[0][0], ck10[1][0], ck10[2][0], ck10[3][0], ck10[4][0])]
ck11_11 = [(text11[0], ck11[0][0], ck11[1][0], ck11[2][0], ck11[3][0], ck11[4][0])]
ck12_12 = [(text12[0], ck12[0][0], ck12[1][0], ck12[2][0], ck12[3][0], ck12[4][0])]
ck13_13 = [(text13[0], ck13[0][0], ck13[1][0], ck13[2][0], ck13[3][0], ck13[4][0])]
ck15_15 = [(text15[0], ck15[0][0], ck15[1][0], ck15[2][0], ck15[3][0], ck15[4][0])]
ck16_16 = [(text16[0], ck16[0][0], ck16[1][0], ck16[2][0], ck16[3][0], ck16[4][0])]
ck17_17 = [(text17[0], ck17[0][0], ck17[1][0], ck17[2][0], ck17[3][0], ck17[4][0])]
ck18_18 = [(text18[0], ck18[0][0], ck18[1][0], ck18[2][0], ck18[3][0], ck18[4][0])]
ck19_19 = [(text19[0], ck19[0][0], ck19[1][0], ck19[2][0], ck19[3][0], ck19[4][0])]
ck20_20 = [(text20[0], ck20[0][0], ck20[1][0], ck20[2][0], ck20[3][0], ck20[4][0])]
ck21_21 = [(text21[0], ck21[0][0], ck21[1][0], ck21[2][0], ck21[3][0], ck21[4][0])]
ck22_22 = [(text22[0], ck22[0][0], ck22[1][0], ck22[2][0], ck22[3][0], ck22[4][0])]

keyword1 = pd.DataFrame(ck1_1, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword2 = pd.DataFrame(ck2_2, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword3 = pd.DataFrame(ck3_3, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword4 = pd.DataFrame(ck4_4, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword5 = pd.DataFrame(ck5_5, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword6 = pd.DataFrame(ck6_6, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword7 = pd.DataFrame(ck7_7, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword8 = pd.DataFrame(ck8_8, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword9 = pd.DataFrame(ck9_9, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword10 = pd.DataFrame(ck10_10, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword11 = pd.DataFrame(ck11_11, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword12 = pd.DataFrame(ck12_12, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword13 = pd.DataFrame(ck13_13, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword15 = pd.DataFrame(ck15_15, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword16 = pd.DataFrame(ck16_16, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword17 = pd.DataFrame(ck17_17, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword18 = pd.DataFrame(ck18_18, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword19 = pd.DataFrame(ck19_19, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword20 = pd.DataFrame(ck20_20, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword21 = pd.DataFrame(ck21_21, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])
keyword22 = pd.DataFrame(ck22_22, columns = ['영화제목','키워드1', '키워드2', '키워드3','키워드4','키워드5'])


keyword = pd.concat([keyword1, keyword2, keyword3, keyword4, keyword5, keyword6, keyword7, keyword8, keyword9, keyword10, keyword11,
                     keyword12, keyword13,  keyword15, keyword16, keyword17, keyword18, keyword19, keyword20, keyword21, keyword22],ignore_index=True)
keyword


# In[ ]:

k1 = keyword[keyword['키워드1'] == '감동']
k2 = keyword[keyword['키워드2'] == '감동'] 
k3 = keyword[keyword['키워드3'] == '감동'] 
k4 = keyword[keyword['키워드4'] == '감동'] 
k5 = keyword[keyword['키워드5'] == '감동']
ks = pd.concat([k1, k2, k3, k4, k5])
print(ks)


