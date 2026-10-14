import streamlit as st
import pandas as pd

# =========================================================
# 기본 설정
# =========================================================
st.set_page_config(
    page_title="KULOKAL",
    page_icon="🍜",
    layout="wide"
)

# =========================================================
# 세션 상태
# =========================================================
if "language" not in st.session_state:
    st.session_state.language = "한국어"

if "user_type" not in st.session_state:
    st.session_state.user_type = None

if "reviews" not in st.session_state:
    st.session_state.reviews = []

if "points" not in st.session_state:
    st.session_state.points = 200


# =========================================================
# 다국어 문구
# =========================================================
TEXT = {
    "한국어": {
        "menu": "메뉴",
        "home": "홈",
        "map": "로컬 맛집 지도",
        "culture": "음식 · 문화",
        "language": "언어 번역",
        "review": "리뷰 · 커뮤니티",
        "recommend": "맞춤 추천",
        "reward": "챌린지 · 리워드",
        "mypage": "마이페이지",

        "intro": "자카르타의 숨은 로컬 음식점과 지역 문화, 언어를 한 곳에서 경험해보세요.",

        "customer": "손님",
        "owner": "사장님",
        "customer_desc": "로컬 맛집을 찾고 음식과 문화를 경험해보세요.",
        "owner_desc": "가게 후기와 고객 반응을 확인할 수 있습니다.",
        "start_customer": "손님으로 시작",
        "start_owner": "사장님으로 시작",

        "restaurants": "등록된 로컬 맛집",
        "foods": "지역 음식",
        "expressions": "번역 표현",
        "popular": "지금 인기 있는 로컬 맛집",

        "map_intro": "자카르타의 다양한 로컬 맛집을 지도에서 확인해보세요.",
        "choose_restaurant": "음식점을 선택하세요",
        "representative_menu": "대표 메뉴",
        "rating": "별점",
        "region": "지역",
        "price": "가격대",
        "mood": "분위기",

        "culture_experience": "지역 문화를 경험할 수 있어요",
        "local_food": "로컬 음식을 경험할 수 있어요",

        "choose_food": "음식을 선택하세요",

        "translation_intro": "식당에서 자주 사용하는 표현을 인도네시아어, 한국어, 영어로 확인해보세요.",
        "choose_phrase": "표현을 선택하세요",

        "visit_restaurant": "방문한 음식점",
        "review_rating": "별점",
        "culture_review": "지역 문화를 잘 느낄 수 있었어요",
        "hidden_review": "숨은 로컬 맛집이에요",
        "friendly_review": "직원이 친절했어요",
        "write_review": "후기를 작성해주세요",
        "submit_review": "리뷰 등록",
        "review_success": "리뷰가 등록되었습니다! +50P",
        "recent_reviews": "최근 후기",
        "no_reviews": "아직 등록된 후기가 없습니다.",

        "recommend_intro": "취향과 상황을 선택하면 조건에 가장 잘 맞는 로컬 맛집 TOP 3를 추천합니다.",
        "spicy_question": "매운맛 선호",
        "budget_question": "1인 예산",
        "food_question": "먹고 싶은 음식 종류",
        "mood_question": "원하는 분위기",
        "purpose_question": "방문 목적",
        "area_question": "원하는 지역",

        "any": "상관없어요",
        "spicy": "매운 음식 좋아해요",
        "not_spicy": "맵지 않은 음식이 좋아요",

        "budget_low": "저렴하게",
        "budget_mid": "보통",
        "budget_high": "가격 상관없음",

        "traditional": "전통적인 분위기",
        "local_favorite": "현지인 맛집",
        "casual": "편안하고 캐주얼",
        "quiet": "조용한 분위기",
        "lively": "활기찬 분위기",

        "solo": "혼밥",
        "date": "데이트",
        "friends": "친구와 함께",
        "family": "가족 식사",

        "recommend_btn": "TOP 3 추천받기",
        "recommend_result": "나에게 맞는 로컬 맛집 TOP 3",
        "recommend_reason": "추천 이유",

        "points": "내 포인트",
        "challenge": "오늘의 챌린지",
        "challenge_text": "현지 언어를 사용해 직접 음식을 주문해보세요!",
        "complete": "챌린지 완료하기",
        "challenge_success": "챌린지 성공! +100P",
        "stamp_tour": "로컬 맛집 스탬프 투어",
        "stamp_caption": "3곳을 모두 방문하면 +500P",

        "login_warning": "홈에서 먼저 손님 또는 사장님을 선택해주세요.",
        "written_reviews": "작성한 리뷰",
        "owner_manage": "사장님 관리",
        "registered_restaurant": "등록 음식점",
        "new_review": "새로운 리뷰가 등록되었습니다.",
        "reset_account": "계정 유형 다시 선택",
        "guest_mode": "손님 모드",
        "owner_mode": "사장님 모드"
    },

    "English": {
        "menu": "Menu",
        "home": "Home",
        "map": "Local Restaurant Map",
        "culture": "Food & Culture",
        "language": "Language Translation",
        "review": "Reviews & Community",
        "recommend": "Recommendations",
        "reward": "Challenges & Rewards",
        "mypage": "My Page",

        "intro": "Discover hidden local restaurants, culture, and language in Jakarta.",

        "customer": "Guest",
        "owner": "Owner",
        "customer_desc": "Discover local restaurants and experience local food and culture.",
        "owner_desc": "Check restaurant reviews and customer reactions.",
        "start_customer": "Start as Guest",
        "start_owner": "Start as Owner",

        "restaurants": "Local Restaurants",
        "foods": "Local Foods",
        "expressions": "Translation Phrases",
        "popular": "Popular Local Restaurants",

        "map_intro": "Explore various local restaurants in Jakarta on the map.",
        "choose_restaurant": "Choose a restaurant",
        "representative_menu": "Signature Menu",
        "rating": "Rating",
        "region": "Area",
        "price": "Price Range",
        "mood": "Atmosphere",

        "culture_experience": "Experience local culture",
        "local_food": "Experience local food",

        "choose_food": "Choose a food",

        "translation_intro": "Check useful restaurant phrases in Indonesian, Korean, and English.",
        "choose_phrase": "Choose a phrase",

        "visit_restaurant": "Restaurant visited",
        "review_rating": "Rating",
        "culture_review": "I could experience local culture",
        "hidden_review": "This is a hidden local restaurant",
        "friendly_review": "The staff were friendly",
        "write_review": "Write your review",
        "submit_review": "Post Review",
        "review_success": "Your review has been posted! +50P",
        "recent_reviews": "Recent Reviews",
        "no_reviews": "There are no reviews yet.",

        "recommend_intro": "Choose your preferences and get your TOP 3 local restaurant recommendations.",
        "spicy_question": "Spice preference",
        "budget_question": "Budget per person",
        "food_question": "Food type",
        "mood_question": "Atmosphere",
        "purpose_question": "Occasion",
        "area_question": "Preferred area",

        "any": "No preference",
        "spicy": "I like spicy food",
        "not_spicy": "I prefer mild food",

        "budget_low": "Budget-friendly",
        "budget_mid": "Moderate",
        "budget_high": "Any price",

        "traditional": "Traditional",
        "local_favorite": "Local favorite",
        "casual": "Casual",
        "quiet": "Quiet",
        "lively": "Lively",

        "solo": "Solo meal",
        "date": "Date",
        "friends": "With friends",
        "family": "Family meal",

        "recommend_btn": "Get TOP 3 Recommendations",
        "recommend_result": "Your TOP 3 Local Restaurants",
        "recommend_reason": "Why we recommend it",

        "points": "My Points",
        "challenge": "Today's Challenge",
        "challenge_text": "Try ordering food using the local language!",
        "complete": "Complete Challenge",
        "challenge_success": "Challenge completed! +100P",
        "stamp_tour": "Local Restaurant Stamp Tour",
        "stamp_caption": "Visit all 3 restaurants to earn +500P",

        "login_warning": "Please select Guest or Owner on the Home page first.",
        "written_reviews": "Reviews written",
        "owner_manage": "Owner Management",
        "registered_restaurant": "Registered Restaurant",
        "new_review": "A new review has been posted.",
        "reset_account": "Change Account Type",
        "guest_mode": "Guest Mode",
        "owner_mode": "Owner Mode"
    },

    "Bahasa Indonesia": {
        "menu": "Menu",
        "home": "Beranda",
        "map": "Peta Kuliner Lokal",
        "culture": "Makanan & Budaya",
        "language": "Terjemahan Bahasa",
        "review": "Ulasan & Komunitas",
        "recommend": "Rekomendasi",
        "reward": "Tantangan & Hadiah",
        "mypage": "Halaman Saya",

        "intro": "Temukan kuliner lokal tersembunyi, budaya, dan bahasa di Jakarta.",

        "customer": "Pengunjung",
        "owner": "Pemilik",
        "customer_desc": "Temukan restoran lokal dan nikmati makanan serta budaya setempat.",
        "owner_desc": "Lihat ulasan restoran dan tanggapan pelanggan.",
        "start_customer": "Mulai sebagai Pengunjung",
        "start_owner": "Mulai sebagai Pemilik",

        "restaurants": "Restoran Lokal",
        "foods": "Makanan Daerah",
        "expressions": "Frasa Terjemahan",
        "popular": "Kuliner Lokal Populer",

        "map_intro": "Jelajahi berbagai restoran lokal di Jakarta melalui peta.",
        "choose_restaurant": "Pilih restoran",
        "representative_menu": "Menu Utama",
        "rating": "Rating",
        "region": "Daerah",
        "price": "Kisaran Harga",
        "mood": "Suasana",

        "culture_experience": "Nikmati budaya lokal",
        "local_food": "Nikmati makanan lokal",

        "choose_food": "Pilih makanan",

        "translation_intro": "Lihat ungkapan yang sering digunakan di restoran dalam bahasa Indonesia, Korea, dan Inggris.",
        "choose_phrase": "Pilih ungkapan",

        "visit_restaurant": "Restoran yang dikunjungi",
        "review_rating": "Rating",
        "culture_review": "Saya dapat merasakan budaya lokal",
        "hidden_review": "Ini adalah restoran lokal tersembunyi",
        "friendly_review": "Stafnya ramah",
        "write_review": "Tulis ulasan Anda",
        "submit_review": "Kirim Ulasan",
        "review_success": "Ulasan berhasil dikirim! +50P",
        "recent_reviews": "Ulasan Terbaru",
        "no_reviews": "Belum ada ulasan.",

        "recommend_intro": "Pilih preferensi Anda dan dapatkan TOP 3 rekomendasi restoran lokal.",
        "spicy_question": "Preferensi rasa pedas",
        "budget_question": "Anggaran per orang",
        "food_question": "Jenis makanan",
        "mood_question": "Suasana",
        "purpose_question": "Tujuan kunjungan",
        "area_question": "Daerah pilihan",

        "any": "Tidak ada preferensi",
        "spicy": "Saya suka makanan pedas",
        "not_spicy": "Saya lebih suka makanan tidak pedas",

        "budget_low": "Hemat",
        "budget_mid": "Sedang",
        "budget_high": "Harga bebas",

        "traditional": "Suasana tradisional",
        "local_favorite": "Favorit warga lokal",
        "casual": "Santai",
        "quiet": "Tenang",
        "lively": "Ramai",

        "solo": "Makan sendiri",
        "date": "Kencan",
        "friends": "Bersama teman",
        "family": "Makan bersama keluarga",

        "recommend_btn": "Dapatkan TOP 3 Rekomendasi",
        "recommend_result": "TOP 3 Restoran Lokal untuk Anda",
        "recommend_reason": "Alasan rekomendasi",

        "points": "Poin Saya",
        "challenge": "Tantangan Hari Ini",
        "challenge_text": "Coba pesan makanan menggunakan bahasa lokal!",
        "complete": "Selesaikan Tantangan",
        "challenge_success": "Tantangan berhasil! +100P",
        "stamp_tour": "Tur Stempel Kuliner Lokal",
        "stamp_caption": "Kunjungi semua 3 restoran untuk mendapatkan +500P",

        "login_warning": "Silakan pilih Pengunjung atau Pemilik di halaman Beranda terlebih dahulu.",
        "written_reviews": "Ulasan yang ditulis",
        "owner_manage": "Manajemen Pemilik",
        "registered_restaurant": "Restoran Terdaftar",
        "new_review": "Ulasan baru telah diterima.",
        "reset_account": "Ubah Jenis Akun",
        "guest_mode": "Mode Pengunjung",
        "owner_mode": "Mode Pemilik"
    }
}


# =========================================================
# 맛집 데이터 - 시연용 12개
# =========================================================
restaurants = [
    {
        "name": "Sari Minang",
        "name_ko": "사리 미낭",
        "food": "Rendang",
        "food_ko": "렌당",
        "emoji": "🍛",
        "area": "Central Jakarta",
        "rating": 4.9,
        "price": "Rp 30,000 ~ 60,000",
        "budget": "mid",
        "category": "Meat",
        "category_ko": "고기",
        "spicy": True,
        "mood": "traditional",
        "purposes": ["family", "friends"],
        "lat": -6.1865,
        "lon": 106.8340
    },
    {
        "name": "Soto Betawi Haji",
        "name_ko": "소토 베타위 하지",
        "food": "Soto Betawi",
        "food_ko": "소토 베타위",
        "emoji": "🥣",
        "area": "Central Jakarta",
        "rating": 4.8,
        "price": "Rp 25,000 ~ 50,000",
        "budget": "mid",
        "category": "Soup",
        "category_ko": "국물요리",
        "spicy": False,
        "mood": "local_favorite",
        "purposes": ["solo", "friends"],
        "lat": -6.1754,
        "lon": 106.8272
    },
    {
        "name": "Gudeg Jakarta",
        "name_ko": "구덱 자카르타",
        "food": "Gudeg",
        "food_ko": "구덱",
        "emoji": "🍲",
        "area": "South Jakarta",
        "rating": 4.7,
        "price": "Rp 20,000 ~ 45,000",
        "budget": "low",
        "category": "Traditional",
        "category_ko": "전통음식",
        "spicy": False,
        "mood": "quiet",
        "purposes": ["solo", "family"],
        "lat": -6.2297,
        "lon": 106.8295
    },
    {
        "name": "Warung Padang Nusantara",
        "name_ko": "와룽 파당 누산타라",
        "food": "Nasi Padang",
        "food_ko": "나시 파당",
        "emoji": "🍚",
        "area": "South Jakarta",
        "rating": 4.7,
        "price": "Rp 25,000 ~ 55,000",
        "budget": "mid",
        "category": "Rice",
        "category_ko": "밥요리",
        "spicy": True,
        "mood": "local_favorite",
        "purposes": ["solo", "friends"],
        "lat": -6.2470,
        "lon": 106.8170
    },
    {
        "name": "Kampung Satay",
        "name_ko": "캄풍 사테",
        "food": "Sate Ayam",
        "food_ko": "사테 아얌",
        "emoji": "🍢",
        "area": "Central Jakarta",
        "rating": 4.6,
        "price": "Rp 20,000 ~ 40,000",
        "budget": "low",
        "category": "Meat",
        "category_ko": "고기",
        "spicy": False,
        "mood": "lively",
        "purposes": ["friends", "family"],
        "lat": -6.1910,
        "lon": 106.8220
    },
    {
        "name": "Bakso Kota",
        "name_ko": "박소 코타",
        "food": "Bakso",
        "food_ko": "박소",
        "emoji": "🥘",
        "area": "West Jakarta",
        "rating": 4.5,
        "price": "Rp 15,000 ~ 35,000",
        "budget": "low",
        "category": "Soup",
        "category_ko": "국물요리",
        "spicy": False,
        "mood": "casual",
        "purposes": ["solo", "friends"],
        "lat": -6.1680,
        "lon": 106.7580
    },
    {
        "name": "Gado Gado Garden",
        "name_ko": "가도 가도 가든",
        "food": "Gado-Gado",
        "food_ko": "가도 가도",
        "emoji": "🥗",
        "area": "South Jakarta",
        "rating": 4.6,
        "price": "Rp 20,000 ~ 45,000",
        "budget": "low",
        "category": "Vegetable",
        "category_ko": "채소요리",
        "spicy": False,
        "mood": "quiet",
        "purposes": ["solo", "date"],
        "lat": -6.2600,
        "lon": 106.8100
    },
    {
        "name": "Ayam Geprek Corner",
        "name_ko": "아얌 게프렉 코너",
        "food": "Ayam Geprek",
        "food_ko": "아얌 게프렉",
        "emoji": "🍗",
        "area": "East Jakarta",
        "rating": 4.5,
        "price": "Rp 20,000 ~ 40,000",
        "budget": "low",
        "category": "Chicken",
        "category_ko": "닭요리",
        "spicy": True,
        "mood": "casual",
        "purposes": ["solo", "friends"],
        "lat": -6.2250,
        "lon": 106.9000
    },
    {
        "name": "Martabak Malam",
        "name_ko": "마르타박 말람",
        "food": "Martabak",
        "food_ko": "마르타박",
        "emoji": "🥞",
        "area": "West Jakarta",
        "rating": 4.8,
        "price": "Rp 30,000 ~ 70,000",
        "budget": "mid",
        "category": "Snack",
        "category_ko": "간식",
        "spicy": False,
        "mood": "lively",
        "purposes": ["date", "friends"],
        "lat": -6.1800,
        "lon": 106.7700
    },
    {
        "name": "Pempek Palembang House",
        "name_ko": "펨펙 팔렘방 하우스",
        "food": "Pempek",
        "food_ko": "펨펙",
        "emoji": "🐟",
        "area": "North Jakarta",
        "rating": 4.6,
        "price": "Rp 25,000 ~ 55,000",
        "budget": "mid",
        "category": "Seafood",
        "category_ko": "해산물",
        "spicy": False,
        "mood": "casual",
        "purposes": ["family", "friends"],
        "lat": -6.1300,
        "lon": 106.8500
    },
    {
        "name": "Rawon Jawa",
        "name_ko": "라원 자와",
        "food": "Rawon",
        "food_ko": "라원",
        "emoji": "🍜",
        "area": "East Jakarta",
        "rating": 4.7,
        "price": "Rp 30,000 ~ 60,000",
        "budget": "mid",
        "category": "Soup",
        "category_ko": "국물요리",
        "spicy": False,
        "mood": "traditional",
        "purposes": ["family", "solo"],
        "lat": -6.2100,
        "lon": 106.8900
    },
    {
        "name": "Nasi Goreng Senja",
        "name_ko": "나시 고렝 센자",
        "food": "Nasi Goreng",
        "food_ko": "나시 고렝",
        "emoji": "🍳",
        "area": "Central Jakarta",
        "rating": 4.8,
        "price": "Rp 20,000 ~ 50,000",
        "budget": "low",
        "category": "Rice",
        "category_ko": "밥요리",
        "spicy": True,
        "mood": "lively",
        "purposes": ["date", "friends"],
        "lat": -6.2000,
        "lon": 106.8200
    }
]


# =========================================================
# 표시용 함수
# =========================================================
def display_restaurant_name(r):
    if st.session_state.language == "한국어":
        return f"{r['name_ko']} ({r['name']})"
    return r["name"]


def display_food_name(r):
    if st.session_state.language == "한국어":
        return f"{r['food_ko']} ({r['food']})"
    return r["food"]


def display_category(r):
    if st.session_state.language == "한국어":
        return r["category_ko"]
    return r["category"]


# =========================================================
# 사이드바
# =========================================================
st.sidebar.title("🍜 KULOKAL")
st.sidebar.caption("Discover Local, Taste the Culture")

language_list = [
    "한국어",
    "English",
    "Bahasa Indonesia"
]

language = st.sidebar.selectbox(
    "🌐 Language",
    language_list,
    index=language_list.index(st.session_state.language)
)

if language != st.session_state.language:
    st.session_state.language = language
    st.rerun()

t = TEXT[st.session_state.language]

menu = st.sidebar.radio(
    t["menu"],
    [
        f"🏠 {t['home']}",
        f"📍 {t['map']}",
        f"🍛 {t['culture']}",
        f"💬 {t['language']}",
        f"⭐ {t['review']}",
        f"✨ {t['recommend']}",
        f"🎁 {t['reward']}",
        f"👤 {t['mypage']}"
    ]
)

st.sidebar.divider()

if st.session_state.user_type == "guest":
    st.sidebar.success(f"🧳 {t['guest_mode']}")

elif st.session_state.user_type == "owner":
    st.sidebar.success(f"🏪 {t['owner_mode']}")


# =========================================================
# 홈
# =========================================================
if menu == f"🏠 {t['home']}":

    st.title("🍜 KULOKAL")
    st.subheader("Discover Local, Taste the Culture")
    st.write(t["intro"])

    st.divider()

    if st.session_state.user_type is None:

        col1, col2 = st.columns(2)

        with col1:
            st.subheader(f"🧳 {t['customer']}")
            st.write(t["customer_desc"])

            if st.button(
                t["start_customer"],
                use_container_width=True
            ):
                st.session_state.user_type = "guest"
                st.rerun()

        with col2:
            st.subheader(f"🏪 {t['owner']}")
            st.write(t["owner_desc"])

            if st.button(
                t["start_owner"],
                use_container_width=True
            ):
                st.session_state.user_type = "owner"
                st.rerun()

    else:

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                t["restaurants"],
                len(restaurants)
            )

        with c2:
            st.metric(
                t["foods"],
                len(set(r["food"] for r in restaurants))
            )

        with c3:
            st.metric(
                t["expressions"],
                "350+"
            )

        st.divider()

        st.header(f"🔥 {t['popular']}")

        ranking = sorted(
            restaurants,
            key=lambda x: x["rating"],
            reverse=True
        )[:5]

        for i, r in enumerate(ranking):

            col1, col2, col3 = st.columns(
                [0.7, 3, 1]
            )

            with col1:
                st.subheader(
                    f"{r['emoji']} #{i + 1}"
                )

            with col2:
                st.write(
                    f"**{display_restaurant_name(r)}**"
                )
                st.caption(
                    f"🍽 {display_food_name(r)} · "
                    f"📍 {r['area']} · "
                    f"✨ {t[r['mood']]}"
                )

            with col3:
                st.metric(
                    t["rating"],
                    r["rating"]
                )

        if (
            st.session_state.user_type == "owner"
            and st.session_state.reviews
        ):
            st.divider()
            st.warning(
                f"🔔 {t['new_review']}"
            )


# =========================================================
# 로컬 맛집 지도
# =========================================================
elif menu == f"📍 {t['map']}":

    st.title(f"📍 {t['map']}")
    st.write(t["map_intro"])

    df = pd.DataFrame(restaurants)

    st.map(
        df,
        latitude="lat",
        longitude="lon"
    )

    st.caption(
        "※ 현재 표시된 음식점 정보는 시연용 프로토타입 데이터입니다."
        if st.session_state.language == "한국어"
        else "※ Restaurant data shown here is for prototype demonstration."
    )

    st.divider()

    restaurant_options = {
        display_restaurant_name(r): r["name"]
        for r in restaurants
    }

    restaurant_display = st.selectbox(
        t["choose_restaurant"],
        list(restaurant_options.keys())
    )

    restaurant_name = restaurant_options[
        restaurant_display
    ]

    selected = next(
        r for r in restaurants
        if r["name"] == restaurant_name
    )

    col1, col2 = st.columns(
        [1, 2]
    )

    with col1:
        st.title(selected["emoji"])
        st.subheader(
            display_food_name(selected)
        )
        st.write(
            f"🏷 {display_category(selected)}"
        )

    with col2:
        st.header(
            display_restaurant_name(selected)
        )

        st.write(
            f"🍽 **{t['representative_menu']}:** "
            f"{display_food_name(selected)}"
        )
        st.write(
            f"⭐ **{t['rating']}:** "
            f"{selected['rating']}"
        )
        st.write(
            f"📍 **{t['region']}:** "
            f"{selected['area']}"
        )
        st.write(
            f"💰 **{t['price']}:** "
            f"{selected['price']}"
        )
        st.write(
            f"✨ **{t['mood']}:** "
            f"{t[selected['mood']]}"
        )

        st.success(
            f"🏺 {t['culture_experience']}"
        )
        st.success(
            f"🍽 {t['local_food']}"
        )


# =========================================================
# 음식 · 문화
# =========================================================
elif menu == f"🍛 {t['culture']}":

    st.title(
        f"🍛 {t['culture']}"
    )

    cultural_foods = [
        restaurants[0],
        restaurants[1],
        restaurants[2],
        restaurants[4],
        restaurants[9],
        restaurants[10]
    ]

    options = {
        display_food_name(r): r
        for r in cultural_foods
    }

    food_display = st.selectbox(
        t["choose_food"],
        list(options.keys())
    )

    selected = options[
        food_display
    ]

    st.title(
        selected["emoji"]
    )

    st.header(
        display_food_name(selected)
    )

    st.write(
        f"📍 {selected['area']}"
    )

    food_key = selected["food"]

    if st.session_state.language == "한국어":

        descriptions = {
            "Rendang":
                "렌당은 고기와 코코넛 밀크, 향신료를 오랜 시간 조리하는 "
                "미낭카바우 지역의 대표적인 전통 음식입니다.",

            "Soto Betawi":
                "소토 베타위는 자카르타의 베타위 문화를 대표하는 "
                "진한 국물 요리입니다.",

            "Gudeg":
                "구덱은 어린 잭프루트를 코코넛 밀크와 향신료로 "
                "천천히 조리하는 족자카르타의 전통 음식입니다.",

            "Sate Ayam":
                "사테 아얌은 닭고기를 꼬치에 끼워 구운 뒤 "
                "땅콩 소스 등과 함께 먹는 인도네시아의 대표적인 음식입니다.",

            "Pempek":
                "펨펙은 팔렘방 지역에서 유래한 생선 반죽 음식으로 "
                "새콤달콤한 소스와 함께 먹는 것이 특징입니다.",

            "Rawon":
                "라원은 진한 색의 국물과 향신료가 특징인 "
                "자바 지역의 전통 소고기 수프입니다."
        }

    elif st.session_state.language == "English":

        descriptions = {
            "Rendang":
                "Rendang is a traditional Minangkabau dish made by slowly cooking "
                "meat with coconut milk and spices.",

            "Soto Betawi":
                "Soto Betawi is a rich traditional soup associated with "
                "Jakarta's Betawi culture.",

            "Gudeg":
                "Gudeg is a traditional Yogyakarta dish made with young jackfruit, "
                "coconut milk, and spices.",

            "Sate Ayam":
                "Sate Ayam is grilled chicken satay commonly served with "
                "peanut sauce and other seasonings.",

            "Pempek":
                "Pempek is a traditional fish cake from Palembang, "
                "usually served with a tangy sweet-and-sour sauce.",

            "Rawon":
                "Rawon is a traditional Javanese beef soup known for "
                "its dark broth and aromatic spices."
        }

    else:

        descriptions = {
            "Rendang":
                "Rendang adalah makanan tradisional Minangkabau yang dimasak "
                "perlahan dengan daging, santan, dan rempah-rempah.",

            "Soto Betawi":
                "Soto Betawi adalah makanan berkuah khas budaya Betawi Jakarta "
                "dengan rasa yang kaya dan gurih.",

            "Gudeg":
                "Gudeg adalah makanan tradisional Yogyakarta yang dibuat "
                "dari nangka muda, santan, dan rempah-rempah.",

            "Sate Ayam":
                "Sate Ayam adalah sate ayam panggang yang biasanya disajikan "
                "dengan saus kacang.",

            "Pempek":
                "Pempek adalah makanan khas Palembang berbahan dasar ikan "
                "yang biasa disajikan dengan kuah cuko.",

            "Rawon":
                "Rawon adalah sup daging sapi khas Jawa dengan kuah gelap "
                "dan aroma rempah yang khas."
        }

    st.write(
        descriptions.get(
            food_key,
            ""
        )
    )

    st.info(
        t["culture_experience"]
    )


# =========================================================
# 언어 번역
# =========================================================
elif menu == f"💬 {t['language']}":

    st.title(
        f"💬 {t['language']}"
    )

    st.write(
        t["translation_intro"]
    )

    phrase_options = {
        "한국어": {
            "안녕하세요": "hello",
            "이거 하나 주세요": "one",
            "감사합니다": "thanks",
            "정말 맛있어요": "delicious",
            "맵지 않게 해주세요": "not_spicy",
            "추천 메뉴가 무엇인가요?": "recommend",
            "계산해주세요": "bill",
            "물 한 병 주세요": "water"
        },

        "English": {
            "Hello": "hello",
            "One of these, please.": "one",
            "Thank you.": "thanks",
            "It's really delicious.": "delicious",
            "Please make it not spicy.": "not_spicy",
            "What do you recommend?": "recommend",
            "The bill, please.": "bill",
            "One bottle of water, please.": "water"
        },

        "Bahasa Indonesia": {
            "Halo": "hello",
            "Saya mau satu ini.": "one",
            "Terima kasih.": "thanks",
            "Sangat enak.": "delicious",
            "Tolong jangan terlalu pedas.": "not_spicy",
            "Menu apa yang Anda rekomendasikan?": "recommend",
            "Minta bon, ya.": "bill",
            "Tolong satu botol air.": "water"
        }
    }

    translations = {
        "hello": {
            "Indonesia": "Halo",
            "Korean": "안녕하세요",
            "English": "Hello"
        },
        "one": {
            "Indonesia": "Saya mau satu ini.",
            "Korean": "이거 하나 주세요",
            "English": "One of these, please."
        },
        "thanks": {
            "Indonesia": "Terima kasih.",
            "Korean": "감사합니다",
            "English": "Thank you."
        },
        "delicious": {
            "Indonesia": "Sangat enak.",
            "Korean": "정말 맛있어요",
            "English": "It's really delicious."
        },
        "not_spicy": {
            "Indonesia": "Tolong jangan terlalu pedas.",
            "Korean": "맵지 않게 해주세요",
            "English": "Please make it not spicy."
        },
        "recommend": {
            "Indonesia": "Menu apa yang Anda rekomendasikan?",
            "Korean": "추천 메뉴가 무엇인가요?",
            "English": "What do you recommend?"
        },
        "bill": {
            "Indonesia": "Minta bon, ya.",
            "Korean": "계산해주세요",
            "English": "The bill, please."
        },
        "water": {
            "Indonesia": "Tolong satu botol air.",
            "Korean": "물 한 병 주세요",
            "English": "One bottle of water, please."
        }
    }

    current_options = phrase_options[
        st.session_state.language
    ]

    selected_display = st.selectbox(
        t["choose_phrase"],
        list(current_options.keys())
    )

    sentence = current_options[
        selected_display
    ]

    c1, c2, c3 = st.columns(3)

    with c1:
        st.subheader(
            "🇮🇩 Bahasa Indonesia"
        )
        st.success(
            translations[sentence]["Indonesia"]
        )

    with c2:
        st.subheader(
            "🇰🇷 한국어"
        )
        st.success(
            translations[sentence]["Korean"]
        )

    with c3:
        st.subheader(
            "🇺🇸 English"
        )
        st.success(
            translations[sentence]["English"]
        )


# =========================================================
# 리뷰 · 커뮤니티
# =========================================================
elif menu == f"⭐ {t['review']}":

    st.title(
        f"⭐ {t['review']}"
    )

    restaurant_options = {
        display_restaurant_name(r): r["name"]
        for r in restaurants
    }

    restaurant_display = st.selectbox(
        t["visit_restaurant"],
        list(restaurant_options.keys())
    )

    restaurant = restaurant_options[
        restaurant_display
    ]

    rating = st.slider(
        f"⭐ {t['review_rating']}",
        1,
        5,
        5
    )

    culture_check = st.checkbox(
        f"🏺 {t['culture_review']}"
    )

    hidden_check = st.checkbox(
        f"💎 {t['hidden_review']}"
    )

    friendly_check = st.checkbox(
        f"😊 {t['friendly_review']}"
    )

    review = st.text_area(
        t["write_review"]
    )

    if st.button(
        t["submit_review"],
        use_container_width=True
    ):

        st.session_state.reviews.append({
            "restaurant": restaurant,
            "rating": rating,
            "review": review,
            "culture": culture_check,
            "hidden": hidden_check,
            "friendly": friendly_check
        })

        st.session_state.points += 50

        st.success(
            f"🎉 {t['review_success']}"
        )

    st.divider()

    st.subheader(
        f"💬 {t['recent_reviews']}"
    )

    if not st.session_state.reviews:

        st.info(
            t["no_reviews"]
        )

    else:

        for item in reversed(
            st.session_state.reviews
        ):

            matched_restaurant = next(
                (
                    r for r in restaurants
                    if r["name"] == item["restaurant"]
                ),
                None
            )

            if matched_restaurant:
                review_title = display_restaurant_name(
                    matched_restaurant
                )
            else:
                review_title = item["restaurant"]

            st.subheader(
                review_title
            )

            st.write(
                "⭐" * item["rating"]
            )

            st.write(
                item["review"]
            )

            tags = []

            if item.get("culture"):
                tags.append(
                    f"🏺 {t['culture_review']}"
                )

            if item.get("hidden"):
                tags.append(
                    f"💎 {t['hidden_review']}"
                )

            if item.get("friendly"):
                tags.append(
                    f"😊 {t['friendly_review']}"
                )

            if tags:
                st.caption(
                    " · ".join(tags)
                )

            st.divider()


# =========================================================
# 맞춤 추천 - 업그레이드
# =========================================================
elif menu == f"✨ {t['recommend']}":

    st.title(
        f"✨ {t['recommend']}"
    )

    st.write(
        t["recommend_intro"]
    )

    st.divider()

    # 1. 매운맛
    spicy_choice = st.selectbox(
        f"🌶 {t['spicy_question']}",
        [
            t["any"],
            t["spicy"],
            t["not_spicy"]
        ]
    )

    # 2. 예산
    budget_choice = st.selectbox(
        f"💰 {t['budget_question']}",
        [
            t["any"],
            t["budget_low"],
            t["budget_mid"],
            t["budget_high"]
        ]
    )

    # 3. 음식 종류
    category_map = {
        t["any"]: None,
        "🍖 고기 / Meat": "Meat",
        "🥣 국물요리 / Soup": "Soup",
        "🍚 밥요리 / Rice": "Rice",
        "🍗 닭요리 / Chicken": "Chicken",
        "🥗 채소요리 / Vegetable": "Vegetable",
        "🐟 해산물 / Seafood": "Seafood",
        "🥞 간식 / Snack": "Snack",
        "🍲 전통음식 / Traditional": "Traditional"
    }

    category_choice_display = st.selectbox(
        f"🍽 {t['food_question']}",
        list(category_map.keys())
    )

    category_choice = category_map[
        category_choice_display
    ]

    # 4. 분위기
    mood_map = {
        t["any"]: None,
        t["traditional"]: "traditional",
        t["local_favorite"]: "local_favorite",
        t["casual"]: "casual",
        t["quiet"]: "quiet",
        t["lively"]: "lively"
    }

    mood_display = st.selectbox(
        f"✨ {t['mood_question']}",
        list(mood_map.keys())
    )

    mood_choice = mood_map[
        mood_display
    ]

    # 5. 방문 목적
    purpose_map = {
        t["any"]: None,
        t["solo"]: "solo",
        t["date"]: "date",
        t["friends"]: "friends",
        t["family"]: "family"
    }

    purpose_display = st.selectbox(
        f"👥 {t['purpose_question']}",
        list(purpose_map.keys())
    )

    purpose_choice = purpose_map[
        purpose_display
    ]

    # 6. 지역
    area_list = sorted(
        set(r["area"] for r in restaurants)
    )

    area_choice = st.selectbox(
        f"📍 {t['area_question']}",
        [t["any"]] + area_list
    )

    st.divider()

    if st.button(
        t["recommend_btn"],
        use_container_width=True
    ):

        results = []

        for r in restaurants:

            score = 0
            reasons = []

            # 매운맛
            if spicy_choice == t["spicy"]:

                if r["spicy"]:
                    score += 2
                    reasons.append(
                        "🌶 매운맛 선호 일치"
                        if st.session_state.language == "한국어"
                        else "🌶 Spice preference match"
                    )

            elif spicy_choice == t["not_spicy"]:

                if not r["spicy"]:
                    score += 2
                    reasons.append(
                        "🌿 맵지 않은 음식 선호 일치"
                        if st.session_state.language == "한국어"
                        else "🌿 Mild food preference match"
                    )

            # 예산
            if budget_choice == t["budget_low"]:

                if r["budget"] == "low":
                    score += 2
                    reasons.append(
                        "💰 저렴한 가격대"
                        if st.session_state.language == "한국어"
                        else "💰 Budget-friendly"
                    )

            elif budget_choice == t["budget_mid"]:

                if r["budget"] in ["low", "mid"]:
                    score += 2
                    reasons.append(
                        "💰 예산 범위 일치"
                        if st.session_state.language == "한국어"
                        else "💰 Budget match"
                    )

            # 음식 종류
            if category_choice is not None:

                if r["category"] == category_choice:
                    score += 3
                    reasons.append(
                        f"🍽 {display_category(r)}"
                    )

            # 분위기
            if mood_choice is not None:

                if r["mood"] == mood_choice:
                    score += 2
                    reasons.append(
                        f"✨ {t[r['mood']]}"
                    )

            # 목적
            if purpose_choice is not None:

                if purpose_choice in r["purposes"]:
                    score += 2
                    reasons.append(
                        f"👥 {purpose_display}"
                    )

            # 지역
            if area_choice != t["any"]:

                if r["area"] == area_choice:
                    score += 3
                    reasons.append(
                        f"📍 {area_choice}"
                    )

            # 기본적으로 별점도 반영
            score += r["rating"] / 10

            results.append({
                "restaurant": r,
                "score": score,
                "reasons": reasons
            })

        results = sorted(
            results,
            key=lambda x: x["score"],
            reverse=True
        )[:3]

        st.success(
            f"🎉 {t['recommend_result']}"
        )

        for rank, result in enumerate(
            results,
            start=1
        ):

            r = result["restaurant"]

            st.subheader(
                f"{rank}위 · {r['emoji']} "
                f"{display_restaurant_name(r)}"
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write(
                    f"🍽 **{display_food_name(r)}**"
                )
                st.write(
                    f"🏷 {display_category(r)}"
                )

            with col2:
                st.write(
                    f"⭐ {r['rating']}"
                )
                st.write(
                    f"📍 {r['area']}"
                )

            with col3:
                st.write(
                    f"💰 {r['price']}"
                )
                st.write(
                    f"✨ {t[r['mood']]}"
                )

            if result["reasons"]:

                st.info(
                    f"💡 {t['recommend_reason']}: "
                    + " · ".join(
                        result["reasons"]
                    )
                )

            else:

                st.info(
                    f"💡 {t['recommend_reason']}: "
                    + (
                        "높은 이용자 평점"
                        if st.session_state.language == "한국어"
                        else "High user rating"
                    )
                )

            st.divider()


# =========================================================
# 챌린지 · 리워드
# =========================================================
elif menu == f"🎁 {t['reward']}":

    st.title(
        f"🎁 {t['reward']}"
    )

    st.metric(
        t["points"],
        f"{st.session_state.points} P"
    )

    st.divider()

    st.subheader(
        f"🎤 {t['challenge']}"
    )

    st.info(
        t["challenge_text"]
    )

    if st.button(
        t["complete"]
    ):

        st.session_state.points += 100

        st.balloons()

        st.success(
            f"🎉 {t['challenge_success']}"
        )

    st.divider()

    st.subheader(
        f"🗺 {t['stamp_tour']}"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(
            f"✅ {display_restaurant_name(restaurants[0])}"
        )

    with col2:
        st.write(
            f"✅ {display_restaurant_name(restaurants[1])}"
        )

    with col3:
        st.write(
            f"⬜ {display_restaurant_name(restaurants[2])}"
        )

    st.progress(
        2 / 3
    )

    st.caption(
        t["stamp_caption"]
    )


# =========================================================
# 마이페이지
# =========================================================
elif menu == f"👤 {t['mypage']}":

    st.title(
        f"👤 {t['mypage']}"
    )

    if st.session_state.user_type is None:

        st.warning(
            t["login_warning"]
        )

    else:

        if st.session_state.user_type == "guest":

            st.subheader(
                f"🧳 {t['customer']}"
            )

        else:

            st.subheader(
                f"🏪 {t['owner']}"
            )

        st.metric(
            t["points"],
            f"{st.session_state.points} P"
        )

        st.write(
            f"📝 {t['written_reviews']}: "
            f"{len(st.session_state.reviews)}"
        )

        if st.session_state.user_type == "owner":

            st.divider()

            st.subheader(
                f"🏪 {t['owner_manage']}"
            )

            st.write(
                f"📍 {t['registered_restaurant']}: "
                f"{display_restaurant_name(restaurants[0])}"
            )

            if st.session_state.reviews:

                st.warning(
                    f"🔔 {t['new_review']}"
                )

        st.divider()

        if st.button(
            t["reset_account"]
        ):

            st.session_state.user_type = None
            st.rerun()
            