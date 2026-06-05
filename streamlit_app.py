import streamlit as st

# 웹 앱 제목 설정
st.title("놀이기구 탑승 가능 여부 확인")
st.write("본인의 키를 입력하고 탑승 가능 여부를 확인하세요.")

# 1. 키 입력 받기 (기본값 150, 최소 0, 최대 250)
height = st.number_input("키(cm)를 입력하세요:", min_value=0, max_value=250, value=150, step=1)

# 2. 확인 버튼 생성 및 조건문 실행
if st.button("탑승 여부 확인"):
    if height < 100:
        st.error('🚫 탑승불가 (100cm 미만)')
    elif height < 130:
        st.warning('⚠️ 보호자 동행시 탑승가능')
    elif height < 195:
        st.success('✅ 탑승가능')
    else:
        st.error('🚫 탑승불가 (195cm 이상)')