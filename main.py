import streamlit as st

st.set_page_config(
    page_title="Personal Color Beauty Store",
    layout="wide"
)

st.markdown("""
<style>
.main-title {
    font-size: 40px;
    font-weight: 800;
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
    border-radius: 18px;
    padding: 15px;
    box-shadow: 0 5px 22px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.product-name {
    font-size: 16px;
    font-weight: 700;
    margin-top: 10px;
}
.category {
    font-size: 12px;
    color: #888;
    margin-top: 4px;
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
    font-weight: 700;
    color: #c40000;
    text-decoration: none;
}
.section-title {
    font-size: 24px;
    font-weight: 800;
    margin: 25px 0 15px 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>Personal Color Beauty Store</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>퍼스널컬러 기반 립 / 블러셔 / 하이라이터 추천</div>", unsafe_allow_html=True)

color = st.selectbox(
    "퍼스널컬러 선택",
    ["봄 웜톤", "여름 쿨톤", "가을 웜톤", "겨울 쿨톤"]
)

base_url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo="

products = {
    "봄 웜톤": [
        {
            "name": "롬앤 쥬시래스팅 틴트 코랄",
            "type": "립",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "goodsNo": "A000000246445",
            "desc": "밝은 코랄 컬러로 얼굴을 화사하게 밝혀주는 대표 봄 웜톤 립"
        },
        {
            "name": "페리페라 코랄 블러셔",
            "type": "블러셔",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "goodsNo": "A000000246446",
            "desc": "생기 있는 코랄 컬러로 자연스러운 혈색 연출"
        },
        {
            "name": "하이라이터 샴페인 골드",
            "type": "하이라이터",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "goodsNo": "A000000246447",
            "desc": "따뜻한 골드빛으로 피부 윤기 강조"
        },
        {
            "name": "에뛰드 살구 틴트",
            "type": "립",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "goodsNo": "A000000246448",
            "desc": "살구빛 MLBB 느낌으로 자연스러운 립"
        },
        {
            "name": "베이스 쿠션 라이트 베이지",
            "type": "베이스",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "goodsNo": "A000000246449",
            "desc": "밝고 투명한 피부 표현"
        },
        {
            "name": "롬앤 피치 글로우 블러셔",
            "type": "블러셔",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "goodsNo": "A000000246450",
            "desc": "피치빛 광채 블러셔로 생기 강화"
        }
    ]
}

st.markdown(f"<div class='section-title'>{color} 추천 제품</div>", unsafe_allow_html=True)

cols = st.columns(3)

for i, p in enumerate(products[color]):
    with cols[i % 3]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.image(p["img"], use_container_width=True)

        st.markdown(f"<div class='product-name'>{p['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='category'>{p['type']}</div>", unsafe_allow_html=True)

        st.markdown(f"<div class='desc'>{p['desc']}</div>", unsafe_allow_html=True)

        link = base_url + p["goodsNo"]

        st.markdown(f"""
        <a class='link' href='{link}' target='_blank'>
        올리브영에서 보기
        </a>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
