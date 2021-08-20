
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from glob import glob
import random
import re

st.set_page_config(
    page_title = 'Photo Contest 2021 v2',
    page_icon = '📷',
)

"""
# 技開・PFC フォトコンテスト ２０２１２
## 写真評価システム
### ランダムに抽出された4枚の写真にいいね👍と思ったものを回答フォームで評価してくてださい
"""

image_dir = "C:/Users/mukot/Desktop/photo/*.jpg"

@st.cache
def image_read(image_dir):

     img_list = glob(image_dir)
     img_pick_list = random.sample(img_list, 4)
     return img_pick_list


four_images = image_read(image_dir)
img_name1 = four_images[0].split("\\")[1]
img_name2 = four_images[1].split("\\")[1]
img_name3 = four_images[2].split("\\")[1]
img_name4 = four_images[3].split("\\")[1]


comment = "ここに写真のコメントが表示される。"

          
with st.form(key='my_form'):
     st.write("いいね👍とおもった写真をえらんでチェックしてください ※複数回答可")

     kpi1, kpi2 = st.beta_columns(2)

     with kpi1:
          img = Image.open(four_images[0])     
          st.image(img, caption=img_name1)
          st.write(comment)
          c_1 = st.checkbox("いいね👍　"+img_name1)
          add_selectbox1 = st.selectbox(
              img_name1+"は何位ですか？",
              ('1位', '2位', '3位', "4位")
          )  


     with kpi2:
          img = Image.open(four_images[1])
          st.image(img, caption=img_name2)
          st.write(comment)
          c_2 = st.checkbox("いいね👍　"+img_name2)
          add_selectbox2 = st.selectbox(
              img_name2+"は何位ですか？",
              ('1位', '2位', '3位', "4位")
          )  

     kpi1, kpi2 = st.beta_columns(2)

     with kpi1:
          img = Image.open(four_images[2])
          st.image(img, caption=img_name3)
          st.write(comment)
          c_3 = st.checkbox("いいね👍　"+img_name3)
          add_selectbox3 = st.selectbox(
              img_name3+"は何位ですか？",
              ('1位', '2位', '3位', "4位")
          )  

     with kpi2:
          img = Image.open(four_images[3])
          st.image(img, caption=img_name4)
          st.write(comment)
          c_4 = st.checkbox("いいね👍　"+img_name4)
          add_selectbox4 = st.selectbox(
              img_name4+"は何位ですか？",
              ('1位', '2位', '3位', "4位")
          )  

     sales_id = st.text_input(label='社員番号を半角で入力してください')
     name = st.text_input('名前を入力してください')
     

     submit_button = st.form_submit_button(label='送信')
     
     #選択した順位のうち数字だけ取り出す
     num1 = int(re.sub("\\D", "",add_selectbox1))
     num2 = int(re.sub("\\D", "",add_selectbox2))
     num3 = int(re.sub("\\D", "",add_selectbox3))
     num4 = int(re.sub("\\D", "",add_selectbox4))

    
if submit_button:
    st.write(add_selectbox1,add_selectbox2,add_selectbox3,add_selectbox4)
    if num1*num2*num3*num4==24 and num1+num2+num3+num4==10:#24=3*(1*2*4)or3*(2*2*2)→(1,2,3,4)or(2,2,2,3)
        st.write(f"{name}さんの評価結果が送信されました。\nご協力ありがとうございました。")
        st.write(sales_id)
        st.write(name)
        st.write(c_1, c_2, c_3, c_4)
        if c_1:
            st.write(img_name1)
        if c_2:
            st.write(img_name2)
        if c_3:
            st.write(img_name3)
        if c_4:
            st.write(img_name4)

    else:
        st.write(f"投票未完了　※同じ順位は選択できません。")
         
