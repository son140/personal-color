import streamlit as st

st.set_page_config(page_title="Personal Color Beauty Store", layout="wide")

st.markdown("""
<style>
body { background-color:#fff5f7; }

.title {
    text-align:center;
    font-size:44px;
    font-weight:900;
    color:#ff4d88;
}

.sub {
    text-align:center;
    color:#888;
    margin-bottom:20px;
}

.card {
    background:white;
    border-radius:22px;
    padding:15px;
    box-shadow:0 6px 25px rgba(255,105,180,0.15);
    margin-bottom:20px;
    transition:0.2s;
}

.card:hover {
    transform:scale(1.02);
}

.name { font-size:16px; font-weight:800; margin-top:10px; }
.type { color:#ff4d88; font-size:13px; font-weight:700; }
.price { color:#222; font-weight:800; margin-top:5px; }
.desc { font-size:13px; color:#555; margin-top:5px; }

.link {
    display:inline-block;
    margin-top:10px;
    background:#ff4d88;
    color:white;
    padding:6px 10px;
    border-radius:10px;
    text-decoration:none;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>💖 Personal Color Beauty Store</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>퍼스널컬러 기반 립 / 블러셔 / 하이라이터 추천</div>", unsafe_allow_html=True)

color = st.selectbox("퍼스널컬러 선택", ["봄 웜톤", "여름 쿨톤", "가을 웜톤", "겨울 쿨톤"])

base_url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo="

# 💥 대량 데이터 (각각 다르게 구성)
products = {
    "봄 웜톤": [
        {
            "name": "롬앤 쥬시래스팅 틴트 07",
            "type": "립",
            "color": "코랄 피치",
            "price": "12,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMG1.jpg",
            "goodsNo": "A000000246445",
            "desc": "화사한 코랄로 생기 폭발"
        },
        {
            "name": "페리페라 잉크 블러셔",
            "type": "블러셔",
            "color": "피치 오렌지",
            "price": "9,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMG2.jpg",
            "goodsNo": "A000000246446",
            "desc": "자연스럽게 혈색 UP"
        },
        {
            "name": "에뛰드 하이라이터",
            "type": "하이라이터",
            "color": "샴페인 골드",
            "price": "11,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMG3.jpg",
            "goodsNo": "A000000246447",
            "desc": "은은한 광채"
        },
        {
            "name": "롬앤 글로스",
            "type": "립글로스",
            "color": "코랄 핑크",
            "price": "13,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMG4.jpg",
            "goodsNo": "A000000246448",
            "desc": "촉촉한 물광 립"
        },
        {
            "name": "클리오 쿠션",
            "type": "베이스",
            "color": "라이트 베이지",
            "price": "28,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMG5.jpg",
            "goodsNo": "A000000246449",
            "desc": "맑은 피부 표현"
        },
    ],

    "여름 쿨톤": [
        {
            "name": "롬앤 베리 틴트",
            "type": "립",
            "color": "라벤더 핑크",
            "price": "12,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMG6.jpg",
            "goodsNo": "A000000246450",
            "desc": "차분한 쿨톤 MLBB"
        },
        {
            "name": "라네즈 블러셔",
            "type": "블러셔",
            "color": "쿨 핑크",
            "price": "18,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMG7.jpg",
            "goodsNo": "A000000246451",
            "desc": "청량한 느낌"
        },
        {
            "name": "에스쁘아 하이라이터",
            "type": "하이라이터",
            "color": "쿨 라벤더",
            "price": "22,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMG8.jpg",
            "goodsNo": "A000000246452",
            "desc": "투명한 광"
        },
    ],

    "가을 웜톤": [
        {
            "name": "브릭 립 틴트",
            "type": "립",
            "color": "브릭 레드",
            "price": "13,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMG9.jpg",
            "goodsNo": "A000000246453",
            "desc": "딥한 분위기"
        },
        {
            "name": "테라코타 블러셔",
            "type": "블러셔",
            "color": "브라운 오렌지",
            "price": "11,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMG10.jpg",
            "goodsNo": "A000000246454",
            "desc": "가을 감성"
        },
    ],

    "겨울 쿨톤": [
        {
            "name": "체리 레드 틴트",
            "type": "립",
            "color": "딥 체리",
            "price": "14,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMG11.jpg",
            "goodsNo": "A000000246455",
            "desc": "강렬한 존재감"
        },
        {
            "name": "쿨 핑크 하이라이터",
            "type": "하이라이터",
            "color": "아이시 핑크",
            "price": "19,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMG12.jpg",
            "goodsNo": "A000000246456",
            "desc": "차가운 광채"
        },
    ]
}

st.markdown(f"## 💄 {color} 추천 제품")

cols = st.columns(3)

for i, p in enumerate(products[color]):
    with cols[i % 3]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.image(p["img"], use_container_width=True)

        st.markdown(f"<div class='name'>{p['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='type'>{p['type']} · {p['color']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='price'>{p['price']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='desc'>{p['desc']}</div>", unsafe_allow_html=True)

        link = base_url + p["goodsNo"]

        st.markdown(f"""
        <a class='link' href='{link}' target='_blank'>
        💖 올리브영 보기
        </a>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
