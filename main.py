import streamlit as st
import random

# 제목과 스타일
st.markdown(
    """
    <h1 style="text-align: center; color: #ff4b4b; font-size: 48px;">
        ✂️🪨📄 가위바위보 게임 🥳🎉
    </h1>
    <h3 style="text-align: center; color: #6a00ff;">
        당신의 선택을 골라주세요!
    </h3>
    """, 
    unsafe_allow_html=True
)

# 선택지
choices = {
    "✂️ 가위": "가위",
    "🪨 바위": "바위",
    "📄 보": "보"
}

# 사용자 선택 UI
user_choice_emoji = st.radio(
    "👇 아래에서 선택하세요!",
    options=list(choices.keys()),
    index=0,
    horizontal=True
)

user_choice = choices[user_choice_emoji]

# 컴퓨터 선택
computer_choice = random.choice(list(choices.values()))

# 승부 판단 함수
def decide_winner(user, comp):
    if user == comp:
        return "무승부 😮"
    elif (user == "가위" and comp == "보") or \
         (user == "바위" and comp == "가위") or \
         (user == "보" and comp == "바위"):
        return "🎉 당신의 승리! 🏆"
    else:
        return "😢 컴퓨터 승리!"

# 버튼 클릭 시 결과 보여주기
if st.button("결과 보기 ▶️"):
    result = decide_winner(user_choice, computer_choice)

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"<h2 style='text-align:center;'>🧑 당신</h2>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align:center; font-size:80px;'>{user_choice_emoji}</h1>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center;'>{user_choice}</h3>", unsafe_allow_html=True)

    with col2:
        # 컴퓨터 이모지 찾기
        comp_emoji = [k for k,v in choices.items() if v == computer_choice][0]
        st.markdown(f"<h2 style='text-align:center;'>🤖 컴퓨터</h2>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align:center; font-size:80px;'>{comp_emoji}</h1>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center;'>{computer_choice}</h3>", unsafe_allow_html=True)

    st.markdown(f"<h2 style='text-align:center; color:#ff6f61;'>{result}</h2>", unsafe_allow_html=True)

# 하단 애니메이션 효과 (Streamlit 자체 애니메이션 없어서 간단하게 글자색 바꾸기)
st.markdown(
    """
    <style>
    @keyframes rainbow {
      0%{color:#ff0000;}
      14%{color:#ff7f00;}
      28%{color:#ffff00;}
      42%{color:#00ff00;}
      56%{color:#0000ff;}
      70%{color:#4b0082;}
      84%{color:#8f00ff;}
      100%{color:#ff0000;}
    }
    .rainbow-text {
      animation: rainbow 5s infinite;
      font-weight: bold;
      font-size: 22px;
      text-align: center;
    }
    </style>
    <p class="rainbow-text">즐거운 가위바위보 시간 되세요! ✨🥳✨</p>
    """,
    unsafe_allow_html=True
)
