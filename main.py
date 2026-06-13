import streamlit as st

st.set_page_config(page_title="Personal Color Beauty Store", layout="wide")

st.markdown("""
<style>
body { background-color: #fff5f7; }

.title {
    text-align:center;
    font-size:42px;
    font-weight:900;
    color:#ff4d88;
}

.card {
    background:white;
    border-radius:20px;
    padding:15px;
    box-shadow:0 6px 25px rgba(255,105,180,0.15);
    margin-bottom:20px;
}

.name { font-weight:800; font-size:16px; }
.type { color:#ff4d88; font-size:13px; }
.desc { font-size:13px; color:#444; }

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

color = st.selectbox("퍼스널컬러 선택", ["봄 웜톤", "여름 쿨톤", "가을 웜톤", "겨울 쿨톤"])

base_url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo="

# 💥 핵심: 각 상품 이미지 "반드시 다르게 넣기"
products = {
    "봄 웜톤": [
        {
            "name": "롬앤 쥬시래스팅 틴트 07",
            "type": "립",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMAGE_A.jpg",
            "goodsNo": "A000000246445",
            "desc": "화사한 코랄 MLBB"
        },
        {
            "name": "페리페라 블러셔 01",
            "type": "블러셔",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMAGE_B.jpg",
            "goodsNo": "A000000246446",
            "desc": "피치 코랄 생기 블러셔"
        },
        {
            "name": "에뛰드 하이라이터",
            "type": "하이라이터",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMAGE_C.jpg",
            "goodsNo": "A000000246447",
            "desc": "은은한 샴페인 광"
        }
    ],

    "여름 쿨톤": [
        {
            "name": "롬앤 베리 틴트",
            "type": "립",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMAGE_D.jpg",
            "goodsNo": "A000000246448",
            "desc": "라벤더 베리 쿨톤"
        },
        {
            "name": "라네즈 블러셔",
            "type": "블러셔",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMAGE_E.jpg",
            "goodsNo": "A000000246449",
            "desc": "쿨 핑크 생기"
        }
    ],

    "가을 웜톤": [
        {
            "name": "브릭 레드 틴트",
            "type": "립",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMAGE_F.jpg",
            "goodsNo": "A000000246450",
            "desc": "딥 브라운 레드"
        }
    ],

    "겨울 쿨톤": [
        {
            "name": "체리 레드 틴트",
            "type": "립",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/IMAGE_G.jpg",
            "goodsNo": "A000000246451",
            "desc": "선명한 쿨 레드"
        }
    ]
}

st.markdown(f"## 💄 {color} 추천 제품")

cols = st.columns(3)

for i, p in enumerate(products[color]):
    with cols[i % 3]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        # 💥 이미지 (각각 다름!)
        st.image(p["img"], use_container_width=True)

        st.markdown(f"<div class='name'>{p['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='type'>{p['type']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='desc'>{p['desc']}</div>", unsafe_allow_html=True)

        link = base_url + p["goodsNo"]

        st.markdown(f"""
        <a class='link' href='{link}' target='_blank'>
        💖 올리브영 보기
        </a>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
