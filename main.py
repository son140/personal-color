import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(
    page_title="Personal Color Beauty Store",
    layout="wide"
)

# 💖 감성 UI
st.markdown("""
<style>
body {
    background-color: #fff5f7;
}

.main-title {
    font-size: 42px;
    font-weight: 900;
    text-align: center;
    color: #ff4d88;
}

.card {
    background: white;
    border-radius: 20px;
    padding: 15px;
    box-shadow: 0 6px 25px rgba(255, 105, 180, 0.15);
    margin-bottom: 20px;
}
.product-name {font-weight:800;}
.category {color:#ff4d88;}
.desc {font-size:13px;}
.link {
    background:#ff4d88;
    color:white;
    padding:6px 10px;
    border-radius:10px;
    text-decoration:none;
    display:inline-block;
    margin-top:10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>💖 Personal Color Beauty Store</div>", unsafe_allow_html=True)

color = st.selectbox(
    "퍼스널컬러 선택",
    ["봄 웜톤", "여름 쿨톤", "가을 웜톤", "겨울 쿨톤"]
)

base_url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo="

# 💖 안정 이미지 함수 (핵심)
def safe_image(url):
    fallback = "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9"
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=3)

        if r.status_code == 200:
            return Image.open(BytesIO(r.content))
        else:
            return fallback
    except:
        return fallback


# 💖 퍼컬 데이터 (이미지 전부 안전하게 유지)
products = {
    "봄 웜톤": [
        {
            "name": "코랄 틴트",
            "type": "립",
            "img": "https://images.unsplash.com/photo-1526045478516-99145907023c",
            "goodsNo": "A000000246445",
            "desc": "화사한 코랄 컬러"
        },
        {
            "name": "피치 블러셔",
            "type": "블러셔",
            "img": "https://images.unsplash.com/photo-1522337660859-02fbefca4702",
            "goodsNo": "A000000246446",
            "desc": "자연스러운 생기"
        }
    ],

    "여름 쿨톤": [
        {
            "name": "라벤더 틴트",
            "type": "립",
            "img": "https://images.unsplash.com/photo-1526045478516-99145907023c",
            "goodsNo": "A000000246447",
            "desc": "차분한 쿨톤 컬러"
        },
        {
            "name": "핑크 블러셔",
            "type": "블러셔",
            "img": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796",
            "goodsNo": "A000000246448",
            "desc": "청량한 핑크"
        }
    ],

    "가을 웜톤": [
        {
            "name": "브릭 립",
            "type": "립",
            "img": "https://images.unsplash.com/photo-1516975080664-ed2fc6a32937",
            "goodsNo": "A000000246449",
            "desc": "딥한 가을 느낌"
        },
        {
            "name": "브라운 블러셔",
            "type": "블러셔",
            "img": "https://images.unsplash.com/photo-1526045478516-99145907023c",
            "goodsNo": "A000000246450",
            "desc": "따뜻한 톤"
        }
    ],

    "겨울 쿨톤": [
        {
            "name": "체리 레드 립",
            "type": "립",
            "img": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796",
            "goodsNo": "A000000246451",
            "desc": "강렬한 레드"
        },
        {
            "name": "쿨 하이라이터",
            "type": "하이라이터",
            "img": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9",
            "goodsNo": "A000000246452",
            "desc": "차가운 광채"
        }
    ]
}

st.markdown(f"## 💄 {color} 추천 제품")

cols = st.columns(3)

for i, p in enumerate(products[color]):
    with cols[i % 3]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        # 💖 이미지 안전 출력
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            r = requests.get(p["img"], headers=headers, timeout=3)

            if r.status_code == 200:
                img = Image.open(BytesIO(r.content))
                st.image(img, use_container_width=True)
            else:
                st.image(p["img"], use_container_width=True)
        except:
            st.image(p["img"], use_container_width=True)

        st.markdown(f"<div class='product-name'>{p['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='category'>{p['type']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='desc'>{p['desc']}</div>", unsafe_allow_html=True)

        link = base_url + p["goodsNo"]

        st.markdown(f"""
        <a class='link' href='{link}' target='_blank'>
        💖 올리브영 보기
        </a>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
