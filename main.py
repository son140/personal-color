import streamlit as st

st.set_page_config(
    page_title="퍼스널컬러 뷰티 추천",
    layout="wide"
)

st.markdown("""
<style>
.main-title {
    font-size: 38px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}
.sub-title {
    text-align: center;
    color: #666;
    margin-bottom: 30px;
}
.card {
    background-color: white;
    border-radius: 16px;
    padding: 16px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.product-name {
    font-size: 18px;
    font-weight: 600;
    margin-top: 10px;
}
.desc {
    font-size: 14px;
    color: #444;
    margin-top: 8px;
    line-height: 1.5;
}
.link {
    display: inline-block;
    margin-top: 10px;
    color: #d60000;
    font-weight: 600;
    text-decoration: none;
}
.section-title {
    font-size: 22px;
    font-weight: 700;
    margin-top: 30px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>Personal Color Beauty Finder</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>퍼스널컬러에 맞는 립 틴트 추천 서비스</div>", unsafe_allow_html=True)

color = st.selectbox(
    "퍼스널컬러를 선택하세요",
    ["봄 웜톤", "여름 쿨톤", "가을 웜톤", "겨울 쿨톤"]
)

# 올리브영 검색 기본 링크 (네가 준 구조)
base_url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo="

products = {
    "봄 웜톤": [
        {
            "name": "롬앤 쥬시래스팅 틴트 코랄 계열",
            "goodsNo": "A000000246445",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "desc": "봄 웜톤은 밝고 따뜻한 색감이 핵심입니다. 코랄, 피치 계열은 얼굴을 화사하게 만들어주고 혈색을 자연스럽게 살려줍니다."
        }
    ],
    "여름 쿨톤": [
        {
            "name": "롬앤 로즈핑크 쥬시 틴트",
            "goodsNo": "A000000246446",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "desc": "여름 쿨톤은 채도가 낮고 부드러운 핑크/로즈 계열이 잘 어울립니다. 피부 톤을 깨끗하고 차분하게 정리해줍니다."
        }
    ],
    "가을 웜톤": [
        {
            "name": "브릭 레드 틴트",
            "goodsNo": "A000000246447",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "desc": "가을 웜톤은 브릭, 테라코타, 누디 브라운 계열이 핵심입니다. 깊고 분위기 있는 인상을 만들어줍니다."
        }
    ],
    "겨울 쿨톤": [
        {
            "name": "체리 레드 쥬시 틴트",
            "goodsNo": "A000000246448",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "desc": "겨울 쿨톤은 고채도 레드, 체리, 플럼 컬러가 가장 잘 어울립니다. 얼굴 대비를 살려 또렷한 인상을 만들어줍니다."
        }
    ]
}

st.markdown(f"<div class='section-title'>{color} 추천 제품</div>", unsafe_allow_html=True)

cols = st.columns(2)

for i, p in enumerate(products[color]):
    with cols[i % 2]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.image(p["img"], use_container_width=True)

        st.markdown(f"<div class='product-name'>{p['name']}</div>", unsafe_allow_html=True)

        st.markdown(f"<div class='desc'>{p['desc']}</div>", unsafe_allow_html=True)

        link = base_url + p["goodsNo"]

        st.markdown(f"""
        <a class='link' href='{link}' target='_blank'>
        올리브영에서 보기
        </a>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
