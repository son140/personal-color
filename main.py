import streamlit as st

st.set_page_config(
    page_title="Personal Color Beauty Shop",
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
    background: #fff;
    border-radius: 16px;
    padding: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.product-title {
    font-size: 16px;
    font-weight: 700;
    margin-top: 10px;
}
.color-box {
    width: 100%;
    height: 10px;
    border-radius: 5px;
    margin-top: 8px;
}
.desc {
    font-size: 13px;
    color: #444;
    margin-top: 8px;
    line-height: 1.5;
}
.link {
    display: inline-block;
    margin-top: 10px;
    font-weight: 600;
    color: #c40000;
    text-decoration: none;
}
.section-title {
    font-size: 22px;
    font-weight: 700;
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>Personal Color Beauty Shop</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>퍼스널컬러에 맞는 립 틴트 & 색상 추천</div>", unsafe_allow_html=True)

color = st.selectbox(
    "퍼스널컬러 선택",
    ["봄 웜톤", "여름 쿨톤", "가을 웜톤", "겨울 쿨톤"]
)

base_url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo="

products = {
    "봄 웜톤": [
        {
            "name": "롬앤 쥬시래스팅 틴트 07 쿨피치",
            "color": "#ffb6a3",
            "goodsNo": "A000000246445",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "desc": "밝은 피치 코랄 컬러로 피부를 화사하게 밝혀주는 대표 봄 웜톤 틴트입니다."
        },
        {
            "name": "페리페라 잉크 더 에어리 벨벳 02",
            "color": "#ff9b9b",
            "goodsNo": "A000000246446",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "desc": "가벼운 핑크 코랄 느낌으로 생기 있는 얼굴 표현 가능"
        },
        {
            "name": "에뛰드 픽싱 틴트 코랄",
            "color": "#ff7f66",
            "goodsNo": "A000000246447",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "desc": "따뜻한 코랄 오렌지로 생기와 혈색 강화"
        },
        {
            "name": "롬앤 글래스팅 워터 틴트",
            "color": "#ff8f7a",
            "goodsNo": "A000000246448",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "desc": "촉촉한 광택감 + 코랄 조합"
        },
        {
            "name": "클리오 매드매트 립",
            "color": "#ff6f61",
            "goodsNo": "A000000246449",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "desc": "선명한 오렌지 레드 계열"
        },
        {
            "name": "롬앤 누디피치 틴트",
            "color": "#ffd1b3",
            "goodsNo": "A000000246450",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "desc": "자연스러운 누디 피치 컬러"
        }
    ]
}

st.markdown(f"<div class='section-title'>{color} 추천 제품</div>", unsafe_allow_html=True)

cols = st.columns(3)

for i, p in enumerate(products[color]):
    with cols[i % 3]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.image(p["img"], use_container_width=True)

        st.markdown(f"<div class='product-title'>{p['name']}</div>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class='color-box' style='background:{p['color']}'></div>
        """, unsafe_allow_html=True)

        st.markdown(f"<div class='desc'>{p['desc']}</div>", unsafe_allow_html=True)

        link = base_url + p["goodsNo"]

        st.markdown(f"""
        <a class='link' href='{link}' target='_blank'>
        올리브영에서 보기
        </a>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
