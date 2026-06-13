import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Personal Color Beauty Store", layout="wide")

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #fff0f6, #fef6ff);
}

.title {
    text-align:center;
    font-size:44px;
    font-weight:900;
    color:#ff4d88;
    margin-bottom:10px;
}

.card {
    background:white;
    border-radius:20px;
    padding:15px;
    box-shadow:0 6px 25px rgba(255,105,180,0.15);
    margin-bottom:20px;
}

.name { font-size:16px; font-weight:800; margin-top:8px; }
.type { color:#ff4d88; font-weight:700; }
.price { font-weight:800; margin-top:5px; }
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

color = st.selectbox("퍼스널컬러 선택", ["봄 웜톤", "여름 쿨톤", "가을 웜톤", "겨울 쿨톤"])

base_url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo="

# 💥 이미지 "진짜 가져오는 함수"
@st.cache_data
def load_image(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        res = requests.get(url, headers=headers, timeout=5)
        return Image.open(BytesIO(res.content))
    except:
        return None


products = {
    "봄 웜톤": [
        {
            "name": "롬앤 코랄 틴트",
            "type": "립",
            "price": "12,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/5248565926099038124.jpg",
            "goodsNo": "A000000246445",
            "desc": "화사한 코랄 컬러"
        },
        {
            "name": "피치 블러셔",
            "type": "블러셔",
            "price": "9,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/5248565926099038124.jpg",
            "goodsNo": "A000000246446",
            "desc": "자연스러운 생기"
        },
        {
            "name": "샴페인 하이라이터",
            "type": "하이라이터",
            "price": "11,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/5248565926099038124.jpg",
            "goodsNo": "A000000246447",
            "desc": "은은한 광채"
        }
    ],

    "여름 쿨톤": [
        {
            "name": "라벤더 틴트",
            "type": "립",
            "price": "12,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/5248565926099038124.jpg",
            "goodsNo": "A000000246448",
            "desc": "차분한 쿨톤"
        },
        {
            "name": "쿨 핑크 블러셔",
            "type": "블러셔",
            "price": "10,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/5248565926099038124.jpg",
            "goodsNo": "A000000246449",
            "desc": "청량한 핑크"
        }
    ],

    "가을 웜톤": [
        {
            "name": "브릭 립",
            "type": "립",
            "price": "13,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/5248565926099038124.jpg",
            "goodsNo": "A000000246450",
            "desc": "딥한 분위기"
        }
    ],

    "겨울 쿨톤": [
        {
            "name": "체리 레드 틴트",
            "type": "립",
            "price": "14,000원",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/5248565926099038124.jpg",
            "goodsNo": "A000000246451",
            "desc": "강렬한 레드"
        }
    ]
}

st.markdown(f"## 💄 {color} 추천 제품")

cols = st.columns(3)

for i, p in enumerate(products[color]):
    with cols[i % 3]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        # 💥 핵심: 진짜 이미지 로딩
        img = load_image(p["img"])

        if img:
            st.image(img, use_container_width=True)
        else:
            st.image(p["img"], use_container_width=True)

        st.markdown(f"<div class='name'>{p['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='type'>{p['type']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='price'>{p['price']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='desc'>{p['desc']}</div>", unsafe_allow_html=True)

        st.markdown(f"""
        <a class='link' href='{base_url + p['goodsNo']}' target='_blank'>
        💖 올리브영 보기
        </a>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
