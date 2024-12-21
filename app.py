# streamlit_app.py

import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = "YOUR_OPENAI_API_KEY"

# Streamlit 페이지 설정
st.set_page_config(page_title="ChatGPT 챗봇", layout="wide")

# 제목 표시
st.title("ChatGPT 챗봇 웹페이지")
st.write("사용자의 질문과 지시에 응답하는 챗봇입니다. 아래 입력창에 질문을 입력해 보세요!")

# 사용자 입력
user_input = st.text_area("질문 또는 지시문 입력", placeholder="여기에 질문이나 지시문을 입력하세요.", height=150)

# 응답 영역
if st.button("응답 받기"):
    if user_input.strip() == "":
        st.warning("입력창이 비어 있습니다. 질문 또는 지시문을 입력하세요!")
    else:
        try:
            # OpenAI API 호출
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            # 응답 추출 및 표시
            bot_reply = response['choices'][0]['message']['content']
            st.subheader("챗봇 응답:")
            st.write(bot_reply)
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")

# 추가 정보
st.markdown("""
---
이 앱은 [OpenAI ChatGPT API](https://platform.openai.com/docs/)를 사용하여 만들어졌습니다.
""")
