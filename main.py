import streamlit as st
import random
from datetime import datetime

# 🎨 귀여운 스타일
st.set_page_config(page_title="🐾 오늘의 운세", page_icon="✨")
st.markdown(
    """
    <style>
    body {
        background-color: #FFF8F0;
    }
    .stApp {
        background-color: #FFF8F0;
        font-family: 'Nanum Pen Script', cursive;
    }
    h1 {
        color: #FF8DAA;
        text-align: center;
    }
    .fortune-box {
        background-color: #FFE4E1;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 2px 2px 10px #f8d7da;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🐻 운세 리스트
fortunes = [
    ("🍀 대박 운세!", "오늘은 뭐든 잘 풀릴 거예요! 모험을 시작해보세요 🌈"),
    ("🌤 무난한 하루", "작은 행복이 쌓이는 하루가 될 거예요 🍵"),
    ("☁️ 약간의 고민", "잠시 쉬어가도 괜찮아요. 당신은 충분히 잘하고 있어요 💛"),
    ("🌧 조심조심!", "작은 실수에 유의하세요. 여유를 가지면 괜찮아질 거예요 ☔"),
    ("✨ 깜짝 선물!", "뜻밖의 행운이 당신을 기다리고 있어요 🎁"),
    ("🌈 인연의 기운", "오늘은 사람들과의 만남에 주목해 보세요 💕"),
]

# 🎀 입력 받기
st.title("🌟 오늘의 운세 🌟")
st.write("안녕하세요! 이름이나 생일을 입력하고 오늘의 귀여운 운세를 확인해보세요 🐰🎈")

user_input = st.text_input("이름이나 생일을 입력해주세요 💌", "")

# 🐾 운세 보여주기
if user_input:
    seed = sum(ord(c) for c in user_input + datetime.today().strftime("%Y-%m-%d"))
    random.seed(seed)
    fortune_title, fortune_text = random.choice(fortunes)

    st.markdown("<div class='fortune-box'>", unsafe_allow_html=True)
    st.subheader(fortune_title)
    st.write(fortune_text)
    st.markdown("</div>", unsafe_allow_html=True)
