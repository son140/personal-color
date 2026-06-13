import streamlit as st

st.set_page_config(page_title="퍼스널컬러 화장품 추천", page_icon="💄", layout="centered")

st.title("💄 퍼스널컬러 화장품 추천 앱")
st.write("퍼스널컬러를 선택하면 어울리는 화장품을 추천해줄게!")

# 퍼스널컬러 선택
color = st.selectbox(
    "퍼스널컬러를 선택하세요",
    ["봄 웜톤", "여름 쿨톤", "가을 웜톤", "겨울 쿨톤"]
)

# 데이터
data = {
    "봄 웜톤": {
        "립": ["코랄 틴트", "피치 립글로스", "살구 립스틱"],
        "블러셔": ["코랄 블러셔", "살구 치크"],
        "베이스": ["밝은 베이지 쿠션"]
    },
    "여름 쿨톤": {
        "립": ["로즈 핑크 틴트", "모브 립", "라벤더 립밤"],
        "블러셔": ["핑크 블러셔", "라일락 치크"],
        "베이스": ["쿨톤 라이트 쿠션"]
    },
    "가을 웜톤": {
        "립": ["브릭 레드", "테라코타 립", "누드 브라운"],
        "블러셔": ["브라운 코랄 블러셔"],
        "베이스": ["내추럴 베이지 쿠션"]
    },
    "겨울 쿨톤": {
        "립": ["딥 레드 립", "체리 레드", "플럼 립"],
        "블러셔": ["쿨 핑크 블러셔"],
        "베이스": ["클리어 쿨 쿠션"]
    }
}

st.divider()

st.subheader(f"✨ {color} 추천 결과")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 💋 립")
    for item in data[color]["립"]:
        st.write("•", item)

with col2:
    st.markdown("### 🌸 블러셔")
    for item in data[color]["블러셔"]:
        st.write("•", item)

with col3:
    st.markdown("### 🧴 베이스")
    for item in data[color]["베이스"]:
        st.write("•", item)

st.divider()

st.subheader("🛍️ 올리브영 바로가기")

# 올리브영 검색 링크
base_url = "https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query="

colA, colB, colC = st.columns(3)

with colA:
    if st.button("립 제품"):
        st.markdown(f"[올리브영 립 검색]({base_url}{color}+립)")

with colB:
    if st.button("블러셔"):
        st.markdown(f"[올리브영 블러셔 검색]({base_url}{color}+블러셔)")

with colC:
    if st.button("베이스"):
        st.markdown(f"[올리브영 쿠션 검색]({base_url}{color}+쿠션)")
