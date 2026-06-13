import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Personal Color Beauty Store", layout="wide")

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #fff0f6, #f7f3ff, #f0fbff);
    font-family: sans-serif;
}

.title {
    text-align: center;
    font-size: 44px;
    font-weight: 800;
    color: #ff4d88;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 15px;
    color: #777;
    margin-bottom: 30px;
}

.card {
    background: rgba(255,255,255,0.9);
    border-radius: 18px;
    padding: 15px;
    box-shadow: 0 6px 25px rgba(255, 105, 180, 0.12);
    margin-bottom: 20px;
    transition: 0.2s;
}

.card:hover {
    transform: translateY(-4px);
}

.name {
    font-size: 16px;
    font-weight: 700;
    color: #222;
    margin-top: 8px;
}

.type {
    font-size: 13px;
    color: #ff4d88;
    font-weight: 600;
}

.meta {
    font-size: 12px;
    color: #666;
    margin-top: 3px;
}

.price {
    font-size: 14px;
    font-weight: 700;
    color: #111;
    margin-top: 6px;
}

.desc {
    font-size: 13px;
    color: #555;
    margin-top: 6px;
    line-height: 1.4;
}

.link {
    display: inline-block;
    margin-top: 10px;
    padding: 7px 12px;
    border-radius: 10px;
    background: #ff4d88;
    color: white;
    text-decoration: none;
    font-weight: 600;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Personal Color Beauty Store</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Discover your perfect tones · curated makeup for your vibe</div>", unsafe_allow_html=True)

color = st.selectbox(
    "Select your personal color type",
    ["Spring Warm Tone", "Summer Cool Tone", "Autumn Warm Tone", "Winter Cool Tone"]
)

base_url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo="


@st.cache_data
def load_image(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=headers, timeout=5)
        return Image.open(BytesIO(r.content))
    except:
        return None


products = {
    "Spring Warm Tone": [
        {
            "name": "Rom&nd Juicy Tint",
            "type": "Lip",
            "color": "Coral Peach",
            "price": "12,000 KRW",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/5248565926099038124.jpg",
            "goodsNo": "A000000246445",
            "desc": "Bright coral shade that brings natural glow."
        },
        {
            "name": "Peripera Blush",
            "type": "Blush",
            "color": "Soft Peach",
            "price": "9,000 KRW",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/5248565926099038124.jpg",
            "goodsNo": "A000000246446",
            "desc": "Fresh and healthy-looking cheeks."
        },
        {
            "name": "Etude Highlighter",
            "type": "Highlighter",
            "color": "Champagne Gold",
            "price": "11,000 KRW",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/5248565926099038124.jpg",
            "goodsNo": "A000000246447",
            "desc": "Soft glow with elegant shine."
        }
    ],

    "Summer Cool Tone": [
        {
            "name": "Rom&nd Berry Tint",
            "type": "Lip",
            "color": "Lavender Pink",
            "price": "12,000 KRW",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/5248565926099038124.jpg",
            "goodsNo": "A000000246448",
            "desc": "Cool muted tone for daily look."
        },
        {
            "name": "Laneige Blush",
            "type": "Blush",
            "color": "Cool Pink",
            "price": "18,000 KRW",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/5248565926099038124.jpg",
            "goodsNo": "A000000246449",
            "desc": "Light and refreshing color mood."
        }
    ],

    "Autumn Warm Tone": [
        {
            "name": "Brick Lip Tint",
            "type": "Lip",
            "color": "Brick Red",
            "price": "13,000 KRW",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/5248565926099038124.jpg",
            "goodsNo": "A000000246450",
            "desc": "Deep and warm autumn vibe."
        }
    ],

    "Winter Cool Tone": [
        {
            "name": "Cherry Red Tint",
            "type": "Lip",
            "color": "Deep Cherry",
            "price": "14,000 KRW",
            "img": "https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2025/11/5248565926099038124.jpg",
            "goodsNo": "A000000246451",
            "desc": "Bold and powerful statement color."
        }
    ]
}

st.markdown(f"## {color} Recommendations")

cols = st.columns(3)

for i, p in enumerate(products[color]):
    with cols[i % 3]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        img = load_image(p["img"])
        if img:
            st.image(img, use_container_width=True)
        else:
            st.image(p["img"], use_container_width=True)

        st.markdown(f"<div class='name'>{p['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='type'>{p['type']} · {p['color']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='price'>{p['price']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='desc'>{p['desc']}</div>", unsafe_allow_html=True)

        st.markdown(f"""
        <a class='link' href='{base_url + p['goodsNo']}' target='_blank'>
        View on Olive Young
        </a>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
