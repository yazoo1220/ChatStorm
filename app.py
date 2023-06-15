import streamlit as st
theme = st.text_input('考えるテーマ')
goal = st.text_input('ゴール')
direction_input = st.selectbox('考える内容',['what','how','imagine'])
direction_message = {
    'what':'何が必要か',
    'how': 'どんな方法があるか',
    'imagine':'なにが連想されるか'
}
direction = direction_message[direction_input]
st.write(direction)
         
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
  
  
frame = f'''

|    |        |       |
|----|--------|-------|
|    |        |       |
|    | {theme} |       |
|    |        |       |

'''

c1.markdown(frame)


         
import streamlit as st
from langchain. chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import (
    HumanMessage,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import openai
from typing import Any, Dict, List


prompt_template = '''
あなたはブレストの内容をマークダウン形式で記述するツールです。
{goal}を達成するために{direction}、{theme}を中心に考えて
3×3のテーブルをmarkdownで作成してください。

例　goalが靴のキャッチコピーを考える、themeが「快適さ」の場合:
|         |         |           |
|---------|-----------|-----------|
|   軽量    |   歩く喜び  |   理想のフィット感   |
|---------|-----------|-----------|
|   快適なクッション  |   快適さ  |   長時間の歩行も快適   |
|---------|-----------|-----------|
|   柔らかいサポート  |  疲れ知らずの歩き心地  |   心地よい履き心地   |

'''
prompt = PromptTemplate(
    input_variables=["goal","theme","direction"], 
    template=prompt_template
)

class SimpleStreamlitCallbackHandler(BaseCallbackHandler):
    """ Copied only streaming part from StreamlitCallbackHandler """
    
    def __init__(self) -> None:
        self.tokens_area = st.empty()
        self.tokens_stream = ""
        
    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Run on new LLM token. Only available when streaming is enabled."""
        self.tokens_stream += token
        self.tokens_area.markdown(self.tokens_stream)

handler = SimpleStreamlitCallbackHandler()

if ask:
    with c1.spinner('typing...'):
        report = []
        chat = ChatOpenAI(streaming=True, temperature=0.9)
        chain = LLMChain(
            llm=chat, 
            prompt=prompt,
            callbacks=[handler]
        )
        res = chain(inputs=[goal, theme, direction]})
    
