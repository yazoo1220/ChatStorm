import streamlit as st
idea = st.text_input('中心となるアイデア')
goal = st.text_input('ゴール')

left, center, right = st.columns(3)

with left:
    l1 = st.empty()
    l2 = st.empty()
    l3 = st.empty()
    
with center:
    c1 = st.empty()
    c2 = st.empty()
    c3 = st.empty()
    
with right:
    r1 = st.empty()
    r2 = st.empty()
    r3 = st.empty()
  
  
frame = '''

| 内容1    | 内容2    | 内容3    |
| 内容4    | 内容5    | 内容6    |
| 内容7    | 内容8    | 内容9    |

'''

c1.markdown(frame)


