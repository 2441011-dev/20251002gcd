import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 최대공약수(GCD) 계산 로직 (유클리드 호제법) 및 과정 기록
def gcd_with_steps(a, b):
    steps = []

    # 유클리드 호제법을 위해 a가 b보다 크도록 조정 (필수는 아니지만 과정 설명을 위해)
    if a < b:
        a, b = b, a

    steps.append(f"시작: 두 수 {a}, {b}")

    while b:
        remainder = a % b
        # 계산 과정을 기록
        steps.append(f"**{a}**를 **{b}**로 나누면 나머지는 **{remainder}**입니다. 다음 단계는 **{b}**와 **{remainder}**의 GCD를 찾습니다.")
        a, b = b, remainder

    steps.append(f"나머지가 0이 되었으므로, 마지막 제수({a})가 최대공약수입니다.")
    return a, steps

# Streamlit 웹 앱의 제목 설정
st.title("🔢 시각적인 최대공약수(GCD) 계산기")
st.markdown("두 개의 자연수를 입력하면 **유클리드 호제법** 과정을 단계별로 시각화하여 보여드립니다.")

# 사용자 입력 받기
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("첫 번째 수", min_value=1, value=100, step=1)

with col2:
    num2 = st.number_input("두 번째 수", min_value=1, value=75, step=1)

# 계산 버튼
if st.button("최대공약수 과정 보기"):
    if num1 is not None and num2 is not None and num1 >= 1 and num2 >= 1:

        # GCD 함수 호출 및 과정 받기
        result, process_steps = gcd_with_steps(int(num1), int(num2))

        st.subheader("📝 계산 과정:")
        st.write("---")

        # 과정 출력
        for i, step in enumerate(process_steps):
            st.info(f"**단계 {i+1}**: {step}")

        st.write("---")
        st.success(f"최종 결과: **{int(num1)}**과 **{int(num2)}**의 최대공약수는 **{result}**입니다.")

        # 시각화 부분: 막대그래프
        st.subheader("📊 입력된 수와 최대공약수 비교")

        fig, ax = plt.subplots(figsize=(8, 4))
        numbers = [int(num1), int(num2), result]
        labels = [f"첫 번째 수 ({int(num1)})", f"두 번째 수 ({int(num2)})", f"GCD ({result})"]
        colors = ['skyblue', 'lightcoral', 'lightgreen']

        ax.bar(labels, numbers, color=colors, width=0.6)

        # 그래프 설정
        max_val = max(numbers)
        ax.set_ylim(0, max_val * 1.1)
        ax.set_ylabel("값")

        # 막대 위에 값 표시
        for i, v in enumerate(numbers):
            ax.text(i, v + max_val * 0.02, str(v), ha='center', va='bottom', fontweight='bold')

        st.pyplot(fig) 

    else:
        st.error("두 수 모두 1 이상의 자연수를 입력해 주세요.")
