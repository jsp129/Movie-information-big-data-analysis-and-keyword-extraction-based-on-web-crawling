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

url1 = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code='
movies = [85578,203097,184571, 85579, 99354, 123519, 125494, 134963, 136898, 137008, 137326, 144379, 151728, 153620, 154449, 154598, 158626, 158885, 161242, 165026, 168298, 172454]
### 7년의 밤, 명탐정 코난: 비색의 탄환, 소울, 신과함께, 지슬, 아가씨, 퍼시빅림, 라라랜드, 레디플레이어원, 리얼, 블랙팬서, 러빙빈센트, 
### 코코, 치인트, 리틀포레스트, 그레이50, 셰잎옾워터, 콜미바이유어네임, 범죄도시, 사라진밤, 지금만나러갑니다, 곤지암

url2 = '&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page='


for i in movies:
    f = open('Movie_'+str(i)+'.txt', 'w')   ### 영화 한개 마다 txt 파일로 저장
    num = i
    response = req.urlopen('https://movie.naver.com/movie/bi/mi/point.nhn?code='+str(num))
    soup = BeautifulSoup(response, 'html.parser')
    title = soup.select_one('title').string
    f.write('######## '+title+' ########'+'\n\n')   ### 영화 제목 출력
    
    response = req.urlopen(url1+str(num)+url2+'1')   ### 댓글창 개수를 뽑아내보자
    soup = BeautifulSoup(response, 'html.parser')    ### 소스 파싱
    score_total = soup.find('div', class_ = 'score_total')    ### 평점 개수 나타난 곳 추출
    limit = score_total.find_all('em')[0]   ### 평점 개수 추출
    page_limit = int(limit.string.replace(',', ''))/10   ### 숫자형식으로 바꿔서 10으로 나눠줌
    page_limit = math.ceil(page_limit)   ### 소숫점 올림

    for j in range(1, page_limit):
        page = j
        response = req.urlopen(url1+str(num)+url2+str(page))
        soup = BeautifulSoup(response, 'html.parser')
        score_result = soup.find('div', class_ = 'score_result')
        lis = score_result.find_all('li')   # 리뷰가 담겨있는 각 마디를 잘라 벡터화
        
        for li in lis:
            score = li.select_one('div.star_score > em')
            reple = li.select_one('div.score_reple > p')
            
            f.write(score.get_text()+' , '+reple.get_text()+'\n' )  ### 평점, 리뷰 출력
    f.close   ### 텍스트 입력 종료


# In[2]:


file = open('C:/Users/user/Documents/Movie_184517.txt', 'r')
f = file.readlines()
f


# In[3]:


import konlpy.tag

with open('C:/Users/user/Documents/Movie_184517.txt', 'r') as f:
    content = f.read()


# In[4]:


filtered_content = content.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')


# In[5]:


Okt = konlpy.tag.Okt()
Okt_morphs = Okt.pos(filtered_content)  # 튜플반환
print(Okt_morphs)


# In[6]:


#komoran = konlpy.tag.Komoran()
#komoran_morphs = komoran.pos(filtered_content)
#print(komoran_morphs)


# In[7]:


Noun_words = []
for word, pos in Okt_morphs:
    if pos == 'Noun':
        Noun_words.append(word)
print(Noun_words)


# In[8]:


from collections import Counter
c = Counter(Noun_words)
print(c.most_common()) 


# In[10]:


stopwords = '영화','관람객','{', '}', '[', ']', '\’', '?', '!', 'ㄴ', 'ㄹ','\"', ')', '(', '...', '\'','은', '는', '이', '가', ',', '.', '아', '휴', '아이구', '아이쿠', '아이고', '어', '나', '우리', '저희', '따라', '의해', '을', '를', '에', '의', '가', '으로', '로', '에게', '뿐이다', '의거하여', '근거하여', '입각하여', '기준으로', '예하면', '예를 들면', '예를 들자면', '저', '소인', '소생', '저희', '지말고', '하지마', '하지마라', '다른', '물론', '또한', '그리고', '비길수 없다', '해서는 안된다', '뿐만 아니라', '만이 아니다', '만은 아니다', '막론하고', '관계없이', '그치지 않다', '그러나', '그런데', '하지만', '든간에', '논하지 않다', '따지지 않다', '설사', '비록', '더라도', '아니면', '만 못하다', '하는 편이 낫다', '불문하고', '향하여', '향해서', '향하다', '쪽으로', '틈타', '이용하여', '타다', '오르다', '제외하고', '이 외에', '이 밖에', '하여야', '비로소', '한다면 몰라도', '외에도', '이곳', '여기', '부터', '기점으로', '따라서', '할 생각이다', '하려고하다', '이리하여', '그리하여', '그렇게 함으로써', '하지만', '일때', '할때', '앞에서', '중에서', '보는데서', '으로써', '로써', '까지', '해야한다', '일것이다', '반드시', '할줄알다', '할수있다', '할수있어', '임에 틀림없다', '한다면', '등', '등등', '제', '겨우', '단지', '다만', '할뿐', '딩동', '댕그', '대해서', '대하여', '대하면', '훨씬', '얼마나', '얼마만큼', '얼마큼', '남짓', '여', '얼마간', '약간', '다소', '좀', '조금', '다수', '몇', '얼마', '지만', '하물며', '또한', '그러나', '그렇지만', '하지만', '이외에도', '대해 말하자면', '뿐이다', '다음에', '반대로', '반대로 말하자면', '이와 반대로', '바꾸어서 말하면', '바꾸어서 한다면', '만약', '그렇지않으면', '까악', '툭', '딱', '삐걱거리다', '보드득', '비걱거리다', '꽈당', '응당', '해야한다', '에 가서', '각', '각각', '여러분', '각종', '각자', '제각기', '하도록하다', '와', '과', '그러므로', '그래서', '고로', '한 까닭에', '하기 때문에', '거니와', '이지만', '대하여', '관하여', '관한', '과연', '실로', '아니나다를가', '생각한대로', '진짜로', '한적이있다', '하곤하였다', '하', '하하', '허허', '아하', '거바', '와', '오', '왜', '어째서', '무엇때문에', '어찌', '하겠는가', '무슨', '어디', '어느곳', '더군다나', '하물며', '더욱이는', '어느때', '언제', '야', '이봐', '어이', '여보시오', '흐흐', '흥', '휴', '헉헉', '헐떡헐떡', '영차', '여차', '어기여차', '끙끙', '아야', '앗', '아야', '콸콸', '졸졸', '좍좍', '뚝뚝', '주룩주룩', '솨', '우르르', '그래도', '또', '그리고', '바꾸어말하면', '바꾸어말하자면', '혹은', '혹시', '답다', '및', '그에 따르는', '때가 되어', '즉', '지든지', '설령', '가령', '하더라도', '할지라도', '일지라도', '지든지', '몇', '거의', '하마터면', '인젠', '이젠', '된바에야', '된이상', '만큼\t어찌됏든', '그위에', '게다가', '점에서 보아', '비추어 보아', '고려하면', '하게될것이다', '일것이다', '비교적', '좀', '보다더', '비하면', '시키다', '하게하다', '할만하다', '의해서', '연이서', '이어서', '잇따라', '뒤따라', '뒤이어', '결국', '의지하여', '기대여', '통하여', '자마자', '더욱더', '불구하고', '얼마든지', '마음대로', '주저하지 않고', '곧', '즉시', '바로', '당장', '하자마자', '밖에 안된다', '하면된다', '그래', '그렇지', '요컨대', '다시 말하자면', '바꿔 말하면', '즉', '구체적으로', '말하자면', '시작하여', '시초에', '이상', '허', '헉', '허걱', '바와같이', '해도좋다', '해도된다', '게다가', '더구나', '하물며', '와르르', '팍', '퍽', '펄렁', '동안', '이래', '하고있었다', '이었다', '에서', '로부터', '까지', '예하면', '했어요', '해요', '함께', '같이', '더불어', '마저', '마저도', '양자', '모두', '습니다', '가까스로', '하려고하다', '즈음하여', '다른', '다른 방면으로', '해봐요', '습니까', '했어요', '말할것도 없고', '무릎쓰고', '개의치않고', '하는것만 못하다', '하는것이 낫다', '매', '매번', '들', '모', '어느것', '어느', '로써', '갖고말하자면', '어디', '어느쪽', '어느것', '어느해', '어느 년도', '라 해도', '언젠가', '어떤것', '어느것', '저기', '저쪽', '저것', '그때', '그럼', '그러면', '요만한걸', '그래', '그때', '저것만큼', '그저', '이르기까지', '할 줄 안다', '할 힘이 있다', '너', '너희', '당신', '어찌', '설마', '차라리', '할지언정', '할지라도', '할망정', '할지언정', '구토하다', '게우다', '토하다', '메쓰겁다', '옆사람', '퉤', '쳇', '의거하여', '근거하여', '의해', '따라', '힘입어', '그', '다음', '버금', '두번째로', '기타', '첫번째로', '나머지는', '그중에서', '견지에서', '형식으로 쓰여', '입장에서', '위해서', '단지', '의해되다', '하도록시키다', '뿐만아니라', '반대로', '전후', '전자', '앞의것', '잠시', '잠깐', '하면서', '그렇지만', '다음에', '그러한즉', '그런즉', '남들', '아무거나', '어찌하든지', '같다', '비슷하다', '예컨대', '이럴정도로', '어떻게', '만약', '만일', '위에서 서술한바와같이', '인 듯하다', '하지 않는다면', '만약에', '무엇', '무슨', '어느', '어떤', '아래윗', '조차', '한데', '그럼에도 불구하고', '여전히', '심지어', '까지도', '조차도', '하지 않도록', '않기 위하여', '때', '시각', '무렵', '시간', '동안', '어때', '어떠한', '하여금', '네', '예', '우선', '누구', '누가 알겠는가', '아무도', '줄은모른다', '줄은 몰랏다', '하는 김에', '겸사겸사', '하는바', '그런 까닭에', '한 이유는', '그러니', '그러니까', '때문에', '그', '너희', '그들', '너희들', '타인', '것', '것들', '너', '위하여', '공동으로', '동시에', '하기 위하여', '어찌하여', '무엇때문에', '붕붕', '윙윙', '나', '우리', '엉엉', '휘익', '윙윙', '오호', '아하', '어쨋든', '만 못하다\t하기보다는', '차라리', '하는 편이 낫다', '흐흐', '놀라다', '상대적으로 말하자면', '마치', '아니라면', '쉿', '그렇지 않으면', '그렇지 않다면', '안 그러면', '아니었다면', '하든지', '아니면', '이라면', '좋아', '알았어', '하는것도', '그만이다', '어쩔수 없다', '하나', '일', '일반적으로', '일단', '한켠으로는', '오자마자', '이렇게되면', '이와같다면', '전부', '한마디', '한항목', '근거로', '하기에', '아울러', '하지 않도록', '않기 위해서', '이르기까지', '이 되다', '로 인하여', '까닭으로', '이유만으로', '이로 인하여', '그래서', '이 때문에', '그러므로', '그런 까닭에', '알 수 있다', '결론을 낼 수 있다', '으로 인하여', '있다', '어떤것', '관계가 있다', '관련이 있다', '연관되다', '어떤것들', '에 대해', '이리하여', '그리하여', '여부', '하기보다는', '하느니', '하면 할수록', '운운', '이러이러하다', '하구나', '하도다', '다시말하면', '다음으로', '에 있다', '에 달려 있다', '우리', '우리들', '오히려', '하기는한데', '어떻게', '어떻해', '어찌됏어', '어때', '어째서', '본대로', '자', '이', '이쪽', '여기', '이것', '이번', '이렇게말하자면', '이런', '이러한', '이와 같은', '요만큼', '요만한 것', '얼마 안 되는 것', '이만큼', '이 정도의', '이렇게 많은 것', '이와 같다', '이때', '이렇구나', '것과 같이', '끼익', '삐걱', '따위', '와 같은 사람들', '부류의 사람들', '왜냐하면', '중의하나', '오직', '오로지', '에 한하다', '하기만 하면', '도착하다', '까지 미치다', '도달하다', '정도에 이르다', '할 지경이다', '결과에 이르다', '관해서는', '여러분', '하고 있다', '한 후', '혼자', '자기', '자기집', '자신', '우에 종합한것과같이', '총적으로 보면', '총적으로 말하면', '총적으로', '대로 하다', '으로서', '참', '그만이다', '할 따름이다', '쿵', '탕탕', '쾅쾅', '둥둥', '봐', '봐라', '아이야', '아니', '와아', '응', '아이', '참나', '년', '월', '일', '령', '영', '일', '이', '삼', '사', '오', '육', '륙', '칠', '팔', '구', '이천육', '이천칠', '이천팔', '이천구', '하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉', '령', '영', ' ㄴ다'
unique_Noun_words = set(Noun_words)
for word in unique_Noun_words:
    if word in stopwords:
        while word in Noun_words: Noun_words.remove(word)  # 최종결과 : Noun_words


# # + 평점, 감상평, 

# In[28]:


print(Noun_words)


# In[11]:


from collections import Counter
c = Counter(Noun_words)
print(c.most_common()) 


# In[12]:


c.most_common()


# In[13]:


len(Noun_words)


# In[14]:


fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
font = fm.FontProperties(fname=fontpath, size=10)
plt.rc('font',family='NanumBarunGothic')
mpl.font_manager._rebuild()

plt.figure(figsize=(17,10))
words = nltk.Text(Noun_words, name='단어 빈도수')
words.plot(50) # 50개만
plt.show()


# In[15]:


c.most_common(5)


# In[16]:


# 영화 순위 메기기
import requests
from bs4 import BeautifulSoup
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
response= requests.get(url)
source = response.text

soup = BeautifulSoup(source, 'html.parser')

top_list = soup.findAll("div",{"class":"tit3"})

index = 1
for i in top_list:
    print(index, i.text.strip())
    index = index+1


# In[17]:


import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import csv
import re

page_dic = {'1990': 17, '1991' : 16, '1992' : 20, '1993': 21, '1994' : 19, '1995' : 17, '1996' : 17, '1997' : 17, '1998' : 15, '1999' : 16, 
            '2000' : 19, '2001' : 17, '2002' : 18, '2003' : 20, '2004' : 38, '2005' : 21, '2006' : 24, '2007' : 26, '2008' : 28, '2009' : 24,
            '2010' : 29, '2011' : 41, '2012' : 44, '2013' : 61, '2014' : 76, '2015' : 71, '2016' : 59, '2017' : 53, '2018' : 50, '2019' : 43,
            '2020' : 37, '2021':17}

def load_soup(dic):
    years = list(dic.keys())
    pages = list(dic.values())

    soup_object = []
    for idx, year in enumerate(years): 
        for page in range(1, pages[idx]+1):
            # print(year ,page)
            base_url = f"https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?open={year}&page={str(page)}"
            response = requests.get(base_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            data_select = soup.select("#old_content > ul > li")
            soup_object.append(data_select)
    return soup_object

def load_movie_id(dic):
    movie_id = []

    for movie_select in load_soup(dic):
        # print(movie_select)
        for data in movie_select:
            movie_id.append(data.select_one('a')['href'].split('=')[1])
    return movie_id

def load_url(subject, movie_num):
    base_url = f'https://movie.naver.com/movie/bi/mi/{subject}.nhn?code={movie_num}'
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    article = soup.select_one('#content > div.article')
    return article

page_dic2 = {'1990': 17, '1991' : 16}
movie_id = load_movie_id(page_dic)
# print(movie_id)
print(len(movie_id))

for idx, movie_num in enumerate(movie_id):
    # print(idx+1)
    basic_article = load_url('basic', movie_num) # 줄거리를 보여주는 페이지
    datail_article = load_url('detail', movie_num) # 출연배우를 보여주는 페이지

    # 19 청불영화에 대한 예외처리
    if basic_article is None:
        continue
    
    # 영화제목
    title = basic_article.select_one('div.mv_info_area > div.mv_info > h3').get_text().replace('\n', '')
    # print(title)

    # 네티즌 점수 
    star_lst = []
    for num in range(1,5):
        if basic_article.select_one(f'div.mv_info_area > div.mv_info > div.main_score > div.score.score_left > div.star_score > a > em:nth-of-type({num})') is not None:
            star = basic_article.select_one(f'div.mv_info_area > div.mv_info > div.main_score > div.score.score_left > div.star_score > a > em:nth-of-type({num})').get_text()
            star_lst.append(str(star))
    # print("".join(i for i in star_lst))

    # 영화 정보리스트
    info_lst = [i.get_text() for i in basic_article.select('div.mv_info_area > div.mv_info > dl > dt')]
    # print(info_lst)

    # 영화 장르
    if '개요()' in info_lst:
        idx = info_lst.index('개요()')
        genre = [i.get_text() for i in basic_article.select(f'div.mv_info_area > div.mv_info > dl > dd:nth-of-type({idx+1}) > p > span:nth-of-type(1) > a')]
    else:
        genre = ""
    # print(genre)

    # 영화 감독
    if '감독' in info_lst:
        idx = info_lst.index('감독')
        if basic_article.select_one(f'div.mv_info_area > div.mv_info > dl > dd:nth-of-type({idx+1}) > p > a') is not None:
            movie_director = basic_article.select_one(f'div.mv_info_area > div.mv_info > dl > dd:nth-of-type({idx+1}) > p > a').get_text()
    else:
        movie_director = ""
    # print(movie_director)

    # 영화 등급
    if '등급' in info_lst:
        idx = info_lst.index('등급')
        movie_rating = basic_article.select_one(f'div.mv_info_area > div.mv_info > dl > dd:nth-of-type({idx+1}) > p > a').get_text()
    else:
        movie_rating = ""
    # print(movie_rating)

    # 영화 출연
    movie_actors = datail_article.select('div.section_group.section_group_frst > div.obj_section.noline > div > div.lst_people_area.height100')
    #content > div.article > div.section_group.section_group_frst > div.obj_section.noline > div > div.lst_people_area.height100
    actor_lst = []

    # 영화배우 count
    actor_counts = datail_article.select('div.section_group.section_group_frst > div.obj_section.noline > div > div.lst_people_area.height100 > ul > li')
    actor_counts = len(actor_counts)

    for actors in movie_actors:
        for num in range(1, actor_counts+1):
            if actors.select_one(f'ul > li:nth-of-type({num}) > div > div > p.in_prt > em').get_text() == '주연':
                if actors.select_one(f'ul > li:nth-of-type({num}) > div > a') is not None:
                    actor = actors.select_one(f'ul > li:nth-of-type({num}) > div > a').get_text()
                    actor_lst.append(actor)
                elif actors.select_one(f'ul > li:nth-of-type({num}) > div > span') is not None:
                    actor = actors.select_one(f'ul > li:nth-of-type({num}) > div > span').get_text()
                    actor_lst.append(actor)
            else:
                break
            
    # 영화 줄거리
    if basic_article.select_one('div.section_group.section_group_frst > div:nth-of-type(1) > div > div > div > h4') is None:
        summary = ""
    else:
        summary = basic_article.select_one('div.section_group.section_group_frst > div:nth-of-type(1) > div > div.story_area > p').get_text().replace('\r', "").replace('\xa0', "")
    # print(summary)

    movie_data = {
        'movie_id' : movie_num,
        'title' : title,
        'star' : "".join(i for i in star_lst),
        'movie_rating' : movie_rating,
        'genre' : genre,
        'director' : movie_director,
        'actors' : actor_lst,
        'summary' : summary
    }

    # print(movie_data, '\n')

    with open('./movie_data2.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['movie_id', 'title', 'star', 'movie_rating',  'genre', 'director', 'actors', 'summary']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writerow(movie_data)


# In[23]:


import pandas as pd
import numpy as np
from ast import literal_eval
import re
movies_pd = pd.read_csv('C:\\Users\\user\\Documents\\movie_data2.csv')
movies_pd.columns = ['movie_id', 'title', 'star', 'movie_rating', 'genre', 'director', 'actors', 'summary']
movies_pd


# In[26]:


is_num = movies_pd['movie_id'] == 168298
nums = movies_pd[is_num]
nums

