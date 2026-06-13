import streamlit as st

st.set_page_config(page_title="퍼스널컬러 뷰티 스토어", layout="wide")

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #fff0f6, #f7f3ff, #f0fbff);
    font-family: sans-serif;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #ff4d88;
    margin-bottom: 6px;
    letter-spacing: 1px;
}

.subtitle {
    text-align: center;
    font-size: 14px;
    color: #777;
    margin-bottom: 30px;
}

.card {
    background: rgba(255,255,255,0.88);
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 18px;
    box-shadow: 0 6px 22px rgba(0,0,0,0.06);
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

st.markdown("<div class='title'>퍼스널컬러 뷰티 스토어</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>당신의 분위기에 어울리는 메이크업을 추천해드립니다</div>", unsafe_allow_html=True)

color = st.selectbox(
    "퍼스널컬러를 선택하세요",
    ["봄 웜톤", "여름 쿨톤", "가을 웜톤", "겨울 쿨톤"]
)

base_url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo="

products = {
    "봄 웜톤": [
        {
            "name": "롬앤 쥬시래스팅 틴트",
            "type": "립",
            "color": "코랄 피치",
            "price": "12,000원",
            "desc": "화사하고 생기 있는 분위기를 만들어주는 대표 코랄 립입니다.",
            "goodsNo": "A000000246445"
        },
        {
            "name": "페리페라 블러셔",
            "type": "블러셔",
            "color": "소프트 피치",
            "price": "9,000원",
            "desc": "자연스럽게 혈색을 살려주는 데일리 블러셔입니다.",
            "goodsNo": "A000000246446"
        },
        {
            "name": "에뛰드 하이라이터",
            "type": "하이라이터",
            "color": "샴페인 골드",
            "price": "11,000원",
            "desc": "부드럽고 은은한 광채를 더해주는 제품입니다.",
            "goodsNo": "A000000246447"
        },
        {
            "name": "글로시 립밤",
            "type": "립",
            "color": "투명 핑크",
            "price": "8,000원",
            "desc": "촉촉한 입술을 유지해주는 데일리 립밤입니다.",
            "goodsNo": "A000000246448"
        },
        {
            "name": "베이스 쿠션",
            "type": "베이스",
            "color": "라이트 베이지",
            "price": "28,000원",
            "desc": "맑고 깨끗한 피부 표현을 도와주는 쿠션입니다.",
            "goodsNo": "A000000246449"
        }
    ],

    "여름 쿨톤": [
        {
            "name": "롬앤 베리 틴트",
            "type": "립",
            "color": "라벤더 핑크",
            "price": "12,000원",
            "desc": "차분하고 부드러운 분위기의 쿨톤 립입니다.",
            "goodsNo": "A000000246450"
        },
        {
            "name": "라네즈 블러셔",
            "type": "블러셔",
            "color": "쿨 핑크",
            "price": "18,000원",
            "desc": "맑고 청량한 느낌을 주는 블러셔입니다.",
            "goodsNo": "A000000246451"
        },
        {
            "name": "에스쁘아 하이라이터",
            "type": "하이라이터",
            "color": "라벤더 광",
            "price": "22,000원",
            "desc": "투명하고 시원한 광채를 연출합니다.",
            "goodsNo": "A000000246452"
        }
    ],

    "가을 웜톤": [
        {
            "name": "브릭 립 틴트",
            "type": "립",
            "color": "브릭 레드",
            "price": "13,000원",
            "desc": "깊이 있고 차분한 가을 분위기 립입니다.",
            "goodsNo": "A000000246453"
        },
        {
            "name": "테라코타 블러셔",
            "type": "블러셔",
            "color": "브라운 오렌지",
            "price": "11,000원",
            "desc": "따뜻하고 분위기 있는 혈색을 연출합니다.",
            "goodsNo": "A000000246454"
        }
    ],

    "겨울 쿨톤": [
        {
            "name": "체리 레드 틴트",
            "type": "립",
            "color": "딥 체리",
            "price": "14,000원",
            "desc": "선명하고 강렬한 존재감을 주는 립입니다.",
            "goodsNo": "A000000246455"
        },
        {
            "name": "쿨 핑크 블러셔",
            "type": "블러셔",
            "color": "아이시 핑크",
            "price": "15,000원",
            "desc": "차갑고 깨끗한 느낌의 블러셔입니다.",
            "goodsNo": "A000000246456"
        }
    ]
}

st.markdown(f"## {color} 추천 제품")

for p in products[color]:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown(f"<div class='name'>{p['name']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='meta'>{p['type']} · {p['color']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='price'>{p['price']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='desc'>{p['desc']}</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <a class='link' href='{base_url + p['goodsNo']}' target='_blank'>
    올리브영에서 보기
    </a>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
