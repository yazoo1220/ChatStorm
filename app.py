import streamlit as st

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
    |||
    |||
    |||
'''

c1.markdown(frame)
