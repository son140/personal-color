import streamlit as st

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
    letter-spacing: 1px;
}

.subtitle {
    text-align: center;
    font-size: 14px;
    color: #777;
    margin-bottom: 30px;
}

.card {
    background: rgba(255,255,255,0.85);
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 18px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.06);
    transition: 0.2s;
}

.card:hover {
    transform: translateY(-3px);
}

.name {
    font-size: 16px;
    font-weight: 700;
    color: #222;
}

.meta {
    font-size: 13px;
    color: #666;
    margin-top: 4px;
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
    line-height: 1.5;
}

.link {
    display: inline-block;
    margin-top: 10px;
    padding: 7px 12px;
    border-radius: 10px;
    background: #ff4d88;
    color: white;
    text-decoration: none;
    font-size: 13px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Personal Color Beauty Store</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Curated beauty recommendations based on your tone</div>", unsafe_allow_html=True)

color = st.selectbox(
    "Select your personal color type",
    ["Spring Warm Tone", "Summer Cool Tone", "Autumn Warm Tone", "Winter Cool Tone"]
)

base_url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo="

products = {
    "Spring Warm Tone": [
        {
            "name": "Rom&nd Juicy Tint",
            "type": "Lip",
            "color": "Coral Peach",
            "price": "12,000 KRW",
            "desc": "Bright coral tone that enhances natural vitality.",
            "goodsNo": "A000000246445"
        },
        {
            "name": "Peripera Blush",
            "type": "Blush",
            "color": "Soft Peach",
            "price": "9,000 KRW",
            "desc": "Natural flush for daily freshness.",
            "goodsNo": "A000000246446"
        },
        {
            "name": "Etude Highlighter",
            "type": "Highlighter",
            "color": "Champagne Gold",
            "price": "11,000 KRW",
            "desc": "Soft glow for radiant skin.",
            "goodsNo": "A000000246447"
        }
    ],

    "Summer Cool Tone": [
        {
            "name": "Rom&nd Berry Tint",
            "type": "Lip",
            "color": "Lavender Pink",
            "price": "12,000 KRW",
            "desc": "Muted cool tone for calm elegance.",
            "goodsNo": "A000000246448"
        },
        {
            "name": "Laneige Blush",
            "type": "Blush",
            "color": "Cool Pink",
            "price": "18,000 KRW",
            "desc": "Light airy pink mood.",
            "goodsNo": "A000000246449"
        }
    ],

    "Autumn Warm Tone": [
        {
            "name": "Brick Lip Tint",
            "type": "Lip",
            "color": "Brick Red",
            "price": "13,000 KRW",
            "desc": "Deep warm autumn mood.",
            "goodsNo": "A000000246450"
        }
    ],

    "Winter Cool Tone": [
        {
            "name": "Cherry Red Tint",
            "type": "Lip",
            "color": "Deep Cherry",
            "price": "14,000 KRW",
            "desc": "Bold high-contrast statement color.",
            "goodsNo": "A000000246451"
        }
    ]
}

st.markdown(f"## {color} Recommendations")

for p in products[color]:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown(f"<div class='name'>{p['name']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='meta'>{p['type']} · {p['color']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='price'>{p['price']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='desc'>{p['desc']}</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <a class='link' href='{base_url + p['goodsNo']}' target='_blank'>
    View Product
    </a>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
