import streamlit as st

st.set_page_config(page_title="Personal Color Beauty Store", layout="wide")

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #fff0f6, #fdf6ff, #f0fbff);
}

.title {
    text-align:center;
    font-size:46px;
    font-weight:900;
    color:#ff5fa2;
    margin-bottom:10px;
}

.sub {
    text-align:center;
    color:#999;
    margin-bottom:25px;
    font-size:15px;
}

.card {
    background: rgba(255,255,255,0.9);
    border-radius:24px;
    padding:15px;
    box-shadow:0 8px 30px rgba(255,105,180,0.12);
    margin-bottom:20px;
    backdrop-filter: blur(6px);
}

.card:hover {
    transform: translateY(-3px);
    transition:0.2s;
}

.name { font-size:16px; font-weight:800; color:#333; margin-top:8px; }
.type { color:#ff4d88; font-size:13px; font-weight:700; }
.price { font-weight:800; color:#222; margin-top:4px; }
.color { font-size:12px; color:#777; }
.desc { font-size:13px; color:#555; margin-top:6px; }

.link {
    display:inline-block;
    margin-top:10px;
    background:linear-gradient(135deg,#ff4d88,#ff7db8);
    color:white;
    padding:7px 12px;
    border-radius:12px;
    text-decoration:none;
    font-weight:700;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>💖 Personal Color Beauty Store</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>퍼스널컬러 기반 뽀용 메이크업 추천 💄✨</div>", unsafe_allow_html=True)

color = st.selectbox("퍼스널컬러 선택", ["봄 웜톤", "여름 쿨톤", "가을 웜톤", "겨울 쿨톤"])

base_url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo="

# 💥 대량 데이터 (퍼컬별 7~8개)
products = {
    "봄 웜톤": [
        {"name":"롬앤 코랄 틴트","type":"립","color":"코랄","price":"12,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/1.jpg","goodsNo":"A1","desc":"화사한 봄 느낌"},
        {"name":"페리페라 피치 블러셔","type":"블러셔","color":"피치","price":"9,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/2.jpg","goodsNo":"A2","desc":"생기 가득"},
        {"name":"에뛰드 하이라이터","type":"하이라이터","color":"샴페인","price":"11,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/3.jpg","goodsNo":"A3","desc":"광채 포인트"},
        {"name":"롬앤 글로스","type":"립글로스","color":"핑크코랄","price":"13,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/4.jpg","goodsNo":"A4","desc":"촉촉 광택"},
        {"name":"클리오 쿠션","type":"베이스","color":"라이트","price":"28,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/5.jpg","goodsNo":"A5","desc":"맑은 피부"},
        {"name":"투쿨포스쿨 블러셔","type":"블러셔","color":"살구","price":"14,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/6.jpg","goodsNo":"A6","desc":"자연 생기"},
        {"name":"웨이크메이크 립","type":"립","color":"코랄핑크","price":"12,500원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/7.jpg","goodsNo":"A7","desc":"봄빛 립"},
    ],

    "여름 쿨톤": [
        {"name":"롬앤 베리 틴트","type":"립","color":"라벤더","price":"12,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/8.jpg","goodsNo":"B1","desc":"차분 쿨톤"},
        {"name":"라네즈 블러셔","type":"블러셔","color":"쿨핑크","price":"18,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/9.jpg","goodsNo":"B2","desc":"청량 느낌"},
        {"name":"에스쁘아 하이라이터","type":"하이라이터","color":"라벤더","price":"22,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/10.jpg","goodsNo":"B3","desc":"투명 광"},
        {"name":"클리오 틴트","type":"립","color":"모브","price":"13,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/11.jpg","goodsNo":"B4","desc":"MLBB"},
        {"name":"3CE 블러셔","type":"블러셔","color":"핑크","price":"15,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/12.jpg","goodsNo":"B5","desc":"여리여리"},
        {"name":"힌스 립","type":"립","color":"쿨로즈","price":"14,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/13.jpg","goodsNo":"B6","desc":"고급스러움"},
        {"name":"롬앤 쿠션","type":"베이스","color":"페어","price":"27,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/14.jpg","goodsNo":"B7","desc":"투명 피부"},
    ],

    "가을 웜톤": [
        {"name":"브릭 틴트","type":"립","color":"브릭","price":"13,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/15.jpg","goodsNo":"C1","desc":"딥 무드"},
        {"name":"테라코타 블러셔","type":"블러셔","color":"브라운","price":"11,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/16.jpg","goodsNo":"C2","desc":"가을 감성"},
        {"name":"맥 립","type":"립","color":"레드브라운","price":"24,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/17.jpg","goodsNo":"C3","desc":"고급 무드"},
        {"name":"나스 블러셔","type":"블러셔","color":"오렌지","price":"32,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/18.jpg","goodsNo":"C4","desc":"세련됨"},
        {"name":"투페이스드 팔레트","type":"아이","color":"브라운","price":"45,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/19.jpg","goodsNo":"C5","desc":"딥 메이크업"},
        {"name":"에뛰드 립","type":"립","color":"누드","price":"10,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/20.jpg","goodsNo":"C6","desc":"차분함"},
        {"name":"웨이크메이크 쿠션","type":"베이스","color":"베이지","price":"26,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/21.jpg","goodsNo":"C7","desc":"매트 피부"},
    ],

    "겨울 쿨톤": [
        {"name":"체리 틴트","type":"립","color":"딥레드","price":"14,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/22.jpg","goodsNo":"D1","desc":"강렬"},
        {"name":"클리오 블러셔","type":"블러셔","color":"쿨핑크","price":"15,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/23.jpg","goodsNo":"D2","desc":"선명"},
        {"name":"맥 립스틱","type":"립","color":"와인","price":"25,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/24.jpg","goodsNo":"D3","desc":"시크"},
        {"name":"에스쁘아 쿠션","type":"베이스","color":"쿨베이지","price":"30,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/25.jpg","goodsNo":"D4","desc":"매끈 피부"},
        {"name":"3CE 립틴트","type":"립","color":"푸시아","price":"16,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/26.jpg","goodsNo":"D5","desc":"강렬 포인트"},
        {"name":"나스 하이라이터","type":"하이라이터","color":"실버","price":"38,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/27.jpg","goodsNo":"D6","desc":"차가운 광"},
        {"name":"롬앤 블러셔","type":"블러셔","color":"모브","price":"13,000원","img":"https://image.oliveyoung.co.kr/cfimages/cf-goods/uploads/images/item/28.jpg","goodsNo":"D7","desc":"쿨 감성"},
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

        st.markdown(f"""
        <a class='link' href='{base_url + p['goodsNo']}' target='_blank'>
        💖 올리브영 보기
        </a>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
