import streamlit as st

st.set_page_config(
    page_title="Personal Color Beauty Store",
    layout="wide"
)

# 💖 핑크 감성 UI
st.markdown("""
<style>
body {
    background-color: #fff5f7;
}

.main-title {
    font-size: 42px;
    font-weight: 900;
    text-align: center;
    margin-bottom: 5px;
    color: #ff4d88;
}

.sub-title {
    text-align: center;
    color: #888;
    margin-bottom: 30px;
    font-size: 16px;
}

.card {
    background: white;
    border-radius: 20px;
    padding: 15px;
    box-shadow: 0 6px 25px rgba(255, 105, 180, 0.15);
    margin-bottom: 20px;
    border: 1px solid #ffe0ea;
}

.product-name {
    font-size: 16px;
    font-weight: 800;
    margin-top: 10px;
    color: #333;
}

.category {
    font-size: 12px;
    color: #ff4d88;
    margin-top: 4px;
    font-weight: 600;
}

.desc {
    font-size: 13px;
    color: #555;
    margin-top: 8px;
    line-height: 1.5;
}

.link {
    display: inline-block;
    margin-top: 10px;
    font-weight: 700;
    color: white;
    background: #ff4d88;
    padding: 6px 10px;
    border-radius: 10px;
    text-decoration: none;
}

.section-title {
    font-size: 24px;
    font-weight: 900;
    margin: 25px 0 15px 0;
    color: #ff2f7a;
}
</style>
""", unsafe_allow_html=True)

# 💖 타이틀
st.markdown("<div class='main-title'>Personal Color Beauty Store</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>퍼스널컬러 기반 립 / 블러셔 / 하이라이터 추천 💄</div>", unsafe_allow_html=True)

# 💖 선택
color = st.selectbox(
    "퍼스널컬러 선택",
    ["봄 웜톤", "여름 쿨톤", "가을 웜톤", "겨울 쿨톤"]
)

base_url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo="

# 💖 전체 퍼컬 데이터 (핵심 수정 부분)
products = {
    "봄 웜톤": [
        {
            "name": "롬앤 쥬시래스팅 틴트 코랄",
            "type": "립",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "goodsNo": "A000000246445",
            "desc": "밝은 코랄 컬러로 생기 있는 봄 느낌"
        },
        {
            "name": "페리페라 코랄 블러셔",
            "type": "블러셔",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "goodsNo": "A000000246446",
            "desc": "자연스러운 생기 코랄 블러셔"
        }
    ],

    "여름 쿨톤": [
        {
            "name": "롬앤 쥬시래스팅 틴트 베리",
            "type": "립",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "goodsNo": "A000000246447",
            "desc": "차분한 라벤더 베리 MLBB"
        },
        {
            "name": "라벤더 블러셔",
            "type": "블러셔",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "goodsNo": "A000000246448",
            "desc": "시원한 라벤더 핑크 느낌"
        }
    ],

    "가을 웜톤": [
        {
            "name": "브릭 레드 립 틴트",
            "type": "립",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "goodsNo": "A000000246449",
            "desc": "딥한 브릭 컬러로 분위기 있는 가을 느낌"
        },
        {
            "name": "테라코타 블러셔",
            "type": "블러셔",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "goodsNo": "A000000246450",
            "desc": "따뜻한 브라운 오렌지 톤"
        }
    ],

    "겨울 쿨톤": [
        {
            "name": "체리 레드 틴트",
            "type": "립",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "goodsNo": "A000000246451",
            "desc": "선명한 체리 레드로 강한 인상"
        },
        {
            "name": "쿨 핑크 하이라이터",
            "type": "하이라이터",
            "img": "https://image.oliveyoung.co.kr/uploads/images/goods/large/10/0000/0024/A00000024644501ko.jpg",
            "goodsNo": "A000000246452",
            "desc": "차가운 핑크 광채"
        }
    ]
}

# 💖 안전장치 (혹시 몰라서)
if color not in products:
    st.error("해당 퍼스널컬러 데이터가 없습니다 😢")
    st.stop()

st.markdown(f"<div class='section-title'>{color} 추천 제품 💕</div>", unsafe_allow_html=True)

cols = st.columns(3)

# 💖 출력
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
        💖 올리브영에서 보기
        </a>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
