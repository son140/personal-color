import streamlit as st

st.set_page_config(
    page_title="Personal Color Beauty Finder",
    layout="wide"
)

st.markdown("""
    <style>
    .title {
        font-size: 40px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }
    .subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 30px;
    }
    .card {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        margin-bottom: 15px;
    }
    .product-name {
        font-size: 18px;
        font-weight: 600;
        margin-top: 10px;
    }
    .link {
        color: #ff4b4b;
        text-decoration: none;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Personal Color Beauty Finder</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Find your perfect makeup match based on your personal color</div>", unsafe_allow_html=True)

color = st.selectbox(
    "Select your personal color",
    ["Spring Warm", "Summer Cool", "Autumn Warm", "Winter Cool"]
)

products = {
    "Spring Warm": [
        {
            "name": "Rom&nd Juicy Lasting Tint - Coral",
            "img": "https://www.oliveyoung.co.kr/uploads/thumbnail/romand_tint.jpg",
            "query": "롬앤 코랄 틴트"
        },
        {
            "name": "Peripera Ink Velvet - Peach",
            "img": "https://www.oliveyoung.co.kr/uploads/thumbnail/peripera_peach.jpg",
            "query": "페리페라 피치 틴트"
        }
    ],
    "Summer Cool": [
        {
            "name": "Rom&nd Juicy Lasting Tint - Rose Pink",
            "img": "https://www.oliveyoung.co.kr/uploads/thumbnail/romand_rose.jpg",
            "query": "롬앤 로즈핑크 틴트"
        },
        {
            "name": "Etude Fixing Tint - Lavender",
            "img": "https://www.oliveyoung.co.kr/uploads/thumbnail/etude_lavender.jpg",
            "query": "에뛰드 라벤더 틴트"
        }
    ],
    "Autumn Warm": [
        {
            "name": "Rom&nd Juicy Lasting Tint - Brick",
            "img": "https://www.oliveyoung.co.kr/uploads/thumbnail/romand_brick.jpg",
            "query": "롬앤 브릭 틴트"
        },
        {
            "name": "Peripera Ink Velvet - Terracotta",
            "img": "https://www.oliveyoung.co.kr/uploads/thumbnail/peripera_terracotta.jpg",
            "query": "페리페라 테라코타 틴트"
        }
    ],
    "Winter Cool": [
        {
            "name": "Rom&nd Juicy Lasting Tint - Cherry",
            "img": "https://www.oliveyoung.co.kr/uploads/thumbnail/romand_cherry.jpg",
            "query": "롬앤 체리 틴트"
        },
        {
            "name": "Etude Fixing Tint - Plum",
            "img": "https://www.oliveyoung.co.kr/uploads/thumbnail/etude_plum.jpg",
            "query": "에뛰드 플럼 틴트"
        }
    ]
}

st.markdown("## Recommended Products")

base_url = "https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query="

cols = st.columns(2)

for i, item in enumerate(products[color]):
    with cols[i % 2]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.image(item["img"], use_container_width=True)

        st.markdown(f"<div class='product-name'>{item['name']}</div>", unsafe_allow_html=True)

        link = base_url + item["query"]

        st.markdown(f"""
            <a class='link' href='{link}' target='_blank'>
                View on Olive Young
            </a>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
