# personal-colorimport streamlit as st

st.set_page_config(page_title="퍼스널컬러 화장품 추천", page_icon="💄")

st.title("💄 퍼스널컬러 기반 화장품 추천")
st.write("퍼스널컬러를 선택하면 어울리는 메이크업 제품을 추천해줄게!")

# 퍼스널컬러 선택
color = st.selectbox(
    "퍼스널컬러를 선택하세요",
    ["봄 웜톤", "여름 쿨톤", "가을 웜톤", "겨울 쿨톤"]
)

# 추천 데이터
recommend = {
    "봄 웜톤": {
        "lip": ["코랄 립틴트", "피치 글로스", "살구 립스틱"],
        "blush": ["코랄 블러셔", "살구 치크"],
        "base": ["밝은 베이지 쿠션"]
    },
    "여름 쿨톤": {
        "lip": ["로즈 핑크 틴트", "모브 립", "라벤더 립밤"],
        "blush": ["핑크 블러셔", "라일락 치크"],
        "base": ["쿨톤 라이트 쿠션"]
    },
    "가을 웜톤": {
        "lip": ["브릭 레드", "테라코타 립", "누드 브라운"],
        "blush": ["코랄 브라운 블러셔"],
        "base": ["내추럴 베이지 파운데이션"]
    },
    "겨울 쿨톤": {
        "lip": ["딥 레드 립", "체리 레드", "플럼 립"],
        "blush": ["쿨 핑크 블러셔"],
        "base": ["클리어 쿨 쿠션"]
    }
}

st.subheader(f"✨ {color} 추천 제품")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 💋 립")
    for item in recommend[color]["lip"]:
        st.write("•", item)

with col2:
    st.markdown("### 🌸 블러셔")
    for item in recommend[color]["blush"]:
        st.write("•", item)

with col3:
    st.markdown("### 🧴 베이스")
    for item in recommend[color]["base"]:
        st.write("•", item)

st.divider()

st.subheader("🛍️ 올리브영에서 찾아보기")

st.write("아래 버튼을 누르면 올리브영에서 바로 검색할 수 있어!")

# 검색 링크 함수
def olive_link(keyword):
    return f"https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query={keyword}"

if st.button("립 제품 보러가기 💋"):
    st.markdown(olive_link(color + " 립"))

if st.button("블러셔 보러가기 🌸"):
    st.markdown(olive_link(color + " 블러셔"))

if st.button("베이스 제품 보러가기 🧴"):
    st.markdown(olive_link(color + " 쿠션"))
