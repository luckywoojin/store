import streamlit as st
import pandas as pd

# 데이터 로드 함수
@st.cache_data
def load_data():
    data = {
        "food_type": ["한식", "한식", "중식", "중식", "양식", "양식"],       # 6개
        "store_name": ["김밥천국", "한솥도시락", "홍콩반점", "동대문엽기짬뽕", "아웃백", "빕스"],  # 6개
        "menu": ["김치찌개", "불고기덮밥", "짜장면", "짬뽕", "스테이크", "파스타"],         # 6개
        "price": [7000, 8000, 6000, 7000, 20000, 15000],                    # 6개
    }
    return pd.DataFrame(data)

# 데이터 로드
data = load_data()

# 페이지 관리
if "page" not in st.session_state:
    st.session_state.page = "home"

# 뒤로 가기 버튼
def back_button(page_name):
    if st.button("뒤로 가기"):
        st.session_state.page = page_name
        st.rerun()

# 음식 유형 선택 페이지
if st.session_state.page == "home":
    st.title("🍴 음식 유형 선택")
    food_types = data["food_type"].unique()
    cols = st.columns(3)  # 3열 격자

    for idx, food_type in enumerate(food_types):
        with cols[idx % 3]:
            if st.button(food_type):
                st.session_state.selected_food_type = food_type
                st.session_state.page = "stores"
                st.rerun()  # 페이지 전환

# 가게 선택 페이지
elif st.session_state.page == "stores":
    st.title(f"🏪 {st.session_state.selected_food_type} 가게 선택")
    filtered_stores = data[data["food_type"] == st.session_state.selected_food_type]
    stores = filtered_stores["store_name"].unique()
    cols = st.columns(3)  # 3열 격자

    for idx, store in enumerate(stores):
        with cols[idx % 3]:
            if st.button(store):
                st.session_state.selected_store = store
                st.session_state.page = "menu"
                st.rerun()  # 페이지 전환

    # 뒤로 가기 버튼 추가
    back_button("home")

# 메뉴 선택 페이지
elif st.session_state.page == "menu":
    st.title(f"📋 {st.session_state.selected_store} 메뉴 보기")
    filtered_menus = data[data["store_name"] == st.session_state.selected_store]

    # 메뉴 목록 출력
    for _, row in filtered_menus.iterrows():
        st.write(f"**{row['menu']}** - {row['price']}원")

    # 뒤로 가기 버튼 추가
    back_button("stores")
