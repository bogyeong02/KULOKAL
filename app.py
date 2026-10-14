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
# 다국어
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

        "map_intro": "자카르타의 숨은 로컬 맛집을 지도에서 확인해보세요.",
        "choose_restaurant": "음식점을 선택하세요",
        "representative_menu": "대표 메뉴",
        "rating": "별점",
        "region": "지역",
        "price": "가격대",
        "mood": "분위기",

        "culture_experience": "지역 문화를 경험할 수 있어요",
        "local_food": "로컬 음식을 경험할 수 있어요",

        "choose_food": "음식을 선택하세요",

        "translation_intro":
            "식당에서 자주 사용하는 표현을 인도네시아어, 한국어, 영어로 확인해보세요.",
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

        "recommend_intro":
            "간단한 취향 선택을 통해 비슷한 분위기의 음식점을 추천합니다.",
        "spicy_question": "매운 음식을 좋아하나요?",
        "spicy_yes": "좋아해요",
        "spicy_no": "별로 안 좋아해요",
        "mood_question": "원하는 분위기는?",
        "traditional": "전통적인 분위기",
        "local_favorite": "현지인 맛집",
        "quiet": "조용한 분위기",
        "recommend_btn": "맛집 추천받기",
        "recommend_success": "취향에 맞는 맛집을 찾았습니다!",

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

        "map_intro": "Discover hidden local restaurants in Jakarta on the map.",
        "choose_restaurant": "Choose a restaurant",
        "representative_menu": "Signature Menu",
        "rating": "Rating",
        "region": "Region",
        "price": "Price Range",
        "mood": "Atmosphere",

        "culture_experience": "Experience local culture",
        "local_food": "Experience local food",

        "choose_food": "Choose a food",

        "translation_intro":
            "Check useful restaurant phrases in Indonesian, Korean, and English.",
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

        "recommend_intro":
            "Choose your preferences and find a restaurant that matches your taste.",
        "spicy_question": "Do you like spicy food?",
        "spicy_yes": "Yes",
        "spicy_no": "Not really",
        "mood_question": "What atmosphere do you prefer?",
        "traditional": "Traditional atmosphere",
        "local_favorite": "Local favorite",
        "quiet": "Quiet atmosphere",
        "recommend_btn": "Get Recommendation",
        "recommend_success": "We found a restaurant for you!",

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

        "map_intro": "Temukan restoran lokal tersembunyi di Jakarta melalui peta.",
        "choose_restaurant": "Pilih restoran",
        "representative_menu": "Menu Utama",
        "rating": "Rating",
        "region": "Daerah",
        "price": "Kisaran Harga",
        "mood": "Suasana",

        "culture_experience": "Nikmati budaya lokal",
        "local_food": "Nikmati makanan lokal",

        "choose_food": "Pilih makanan",

        "translation_intro":
            "Lihat ungkapan yang sering digunakan di restoran dalam bahasa Indonesia, Korea, dan Inggris.",
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

        "recommend_intro":
            "Pilih preferensi Anda untuk menemukan restoran yang sesuai dengan selera Anda.",
        "spicy_question": "Apakah Anda suka makanan pedas?",
        "spicy_yes": "Ya",
        "spicy_no": "Tidak terlalu",
        "mood_question": "Suasana seperti apa yang Anda inginkan?",
        "traditional": "Suasana tradisional",
        "local_favorite": "Favorit warga lokal",
        "quiet": "Suasana tenang",
        "recommend_btn": "Dapatkan Rekomendasi",
        "recommend_success": "Kami menemukan restoran yang cocok untuk Anda!",

        "points": "Poin Saya",
        "challenge": "Tantangan Hari Ini",
        "challenge_text": "Coba pesan makanan menggunakan bahasa lokal!",
        "complete": "Selesaikan Tantangan",
        "challenge_success": "Tantangan berhasil! +100P",
        "stamp_tour": "Tur Stempel Kuliner Lokal",
        "stamp_caption": "Kunjungi semua 3 restoran untuk mendapatkan +500P",

        "login_warning":
            "Silakan pilih Pengunjung atau Pemilik di halaman Beranda terlebih dahulu.",
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
# 음식점 데이터
# =========================================================
restaurants = [
    {
        "name": "Sari Minang",
        "name_ko": "사리 미낭",
        "food": "Rendang",
        "food_ko": "렌당",
        "emoji": "🍛",
        "region": "West Sumatra",
        "rating": 4.9,
        "price": "Rp 30,000 ~ 60,000",
        "mood_key": "traditional",
        "lat": -6.2000,
        "lon": 106.8166
    },
    {
        "name": "Soto Betawi Haji",
        "name_ko": "소토 베타위 하지",
        "food": "Soto Betawi",
        "food_ko": "소토 베타위",
        "emoji": "🥣",
        "region": "Jakarta",
        "rating": 4.8,
        "price": "Rp 25,000 ~ 50,000",
        "mood_key": "local_favorite",
        "lat": -6.1754,
        "lon": 106.8272
    },
    {
        "name": "Gudeg Jakarta",
        "name_ko": "구덱 자카르타",
        "food": "Gudeg",
        "food_ko": "구덱",
        "emoji": "🍲",
        "region": "Yogyakarta",
        "rating": 4.7,
        "price": "Rp 20,000 ~ 45,000",
        "mood_key": "quiet",
        "lat": -6.2297,
        "lon": 106.8295
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
    index=language_list.index(
        st.session_state.language
    )
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
    st.sidebar.success(
        f"🧳 {t['guest_mode']}"
    )

elif st.session_state.user_type == "owner":
    st.sidebar.success(
        f"🏪 {t['owner_mode']}"
    )


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
            st.subheader(
                f"🧳 {t['customer']}"
            )
            st.write(
                t["customer_desc"]
            )

            if st.button(
                t["start_customer"],
                use_container_width=True
            ):
                st.session_state.user_type = "guest"
                st.rerun()

        with col2:
            st.subheader(
                f"🏪 {t['owner']}"
            )
            st.write(
                t["owner_desc"]
            )

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
                "128"
            )

        with c2:
            st.metric(
                t["foods"],
                "42"
            )

        with c3:
            st.metric(
                t["expressions"],
                "350+"
            )

        st.divider()

        st.header(
            f"🔥 {t['popular']}"
        )

        ranking = sorted(
            restaurants,
            key=lambda x: x["rating"],
            reverse=True
        )

        cols = st.columns(3)

        for i, r in enumerate(ranking):

            with cols[i]:
                st.subheader(
                    f"{r['emoji']} #{i + 1}"
                )
                st.write(
                    f"**{display_restaurant_name(r)}**"
                )
                st.write(
                    f"🍽 {display_food_name(r)}"
                )
                st.write(
                    f"⭐ {r['rating']}"
                )
                st.write(
                    f"📍 {r['region']}"
                )
                st.write(
                    f"✨ {t[r['mood_key']]}"
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

    st.title(
        f"📍 {t['map']}"
    )

    st.write(
        t["map_intro"]
    )

    df = pd.DataFrame(
        restaurants
    )

    st.map(
        df,
        latitude="lat",
        longitude="lon"
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
        r
        for r in restaurants
        if r["name"] == restaurant_name
    )

    col1, col2 = st.columns(
        [1, 2]
    )

    with col1:
        st.title(
            selected["emoji"]
        )
        st.subheader(
            display_food_name(selected)
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
            f"{selected['region']}"
        )
        st.write(
            f"💰 **{t['price']}:** "
            f"{selected['price']}"
        )
        st.write(
            f"✨ **{t['mood']}:** "
            f"{t[selected['mood_key']]}"
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

    food_options = {
        "한국어": {
            "렌당 (Rendang)": "rendang",
            "소토 베타위 (Soto Betawi)": "soto",
            "구덱 (Gudeg)": "gudeg"
        },

        "English": {
            "Rendang": "rendang",
            "Soto Betawi": "soto",
            "Gudeg": "gudeg"
        },

        "Bahasa Indonesia": {
            "Rendang": "rendang",
            "Soto Betawi": "soto",
            "Gudeg": "gudeg"
        }
    }

    options = food_options[
        st.session_state.language
    ]

    food_display = st.selectbox(
        t["choose_food"],
        list(options.keys())
    )

    food = options[
        food_display
    ]

    if food == "rendang":

        st.title("🍛")

        if st.session_state.language == "한국어":
            st.header("렌당 (Rendang)")
        else:
            st.header("Rendang")

        st.write("📍 West Sumatra")

        if st.session_state.language == "한국어":
            st.write(
                "렌당은 고기와 코코넛 밀크, 향신료를 오랜 시간 조리해 만드는 "
                "서수마트라 미낭카바우 지역의 대표적인 전통 음식입니다."
            )
            st.info(
                "가족 행사나 공동체 모임에서 함께 나누어 먹는 음식으로, "
                "지역의 전통과 공동체 문화를 보여주는 음식입니다."
            )

        elif st.session_state.language == "English":
            st.write(
                "Rendang is a traditional Minangkabau dish from West Sumatra. "
                "It is made by slowly cooking meat with coconut milk and spices."
            )
            st.info(
                "It is often served during family gatherings and community events "
                "and reflects Minangkabau culture."
            )

        else:
            st.write(
                "Rendang adalah makanan tradisional Minangkabau dari Sumatra Barat. "
                "Rendang dibuat dengan memasak daging, santan, dan rempah-rempah "
                "secara perlahan."
            )
            st.info(
                "Rendang sering disajikan dalam acara keluarga dan kegiatan masyarakat "
                "serta mencerminkan budaya Minangkabau."
            )

    elif food == "soto":

        st.title("🥣")

        if st.session_state.language == "한국어":
            st.header("소토 베타위 (Soto Betawi)")
        else:
            st.header("Soto Betawi")

        st.write("📍 Jakarta")

        if st.session_state.language == "한국어":
            st.write(
                "소토 베타위는 자카르타의 베타위 문화를 대표하는 전통 국물 음식입니다. "
                "고기와 향신료를 넣은 진한 국물이 특징입니다."
            )
            st.info(
                "자카르타 지역의 전통적인 식문화를 경험할 수 있는 대표적인 음식입니다."
            )

        elif st.session_state.language == "English":
            st.write(
                "Soto Betawi is a traditional soup associated with the Betawi culture "
                "of Jakarta. It is known for its rich broth, meat, and spices."
            )
            st.info(
                "It is one of Jakarta's representative local dishes."
            )

        else:
            st.write(
                "Soto Betawi adalah makanan berkuah tradisional yang berasal dari "
                "budaya Betawi di Jakarta. Makanan ini dikenal dengan kuah yang gurih, "
                "daging, dan rempah-rempah."
            )
            st.info(
                "Soto Betawi merupakan salah satu makanan khas yang mencerminkan "
                "budaya kuliner Jakarta."
            )

    else:

        st.title("🍲")

        if st.session_state.language == "한국어":
            st.header("구덱 (Gudeg)")
        else:
            st.header("Gudeg")

        st.write("📍 Yogyakarta")

        if st.session_state.language == "한국어":
            st.write(
                "구덱은 어린 잭프루트를 코코넛 밀크와 향신료로 천천히 조리한 "
                "족자카르타의 대표적인 전통 음식입니다."
            )
            st.info(
                "달콤한 맛이 특징이며 족자카르타의 대표적인 지역 음식으로 알려져 있습니다."
            )

        elif st.session_state.language == "English":
            st.write(
                "Gudeg is a traditional dish from Yogyakarta made by slowly cooking "
                "young jackfruit with coconut milk and spices."
            )
            st.info(
                "It is known for its slightly sweet flavor and is one of Yogyakarta's "
                "most iconic local dishes."
            )

        else:
            st.write(
                "Gudeg adalah makanan tradisional khas Yogyakarta yang dibuat dari "
                "nangka muda yang dimasak perlahan dengan santan dan rempah-rempah."
            )
            st.info(
                "Gudeg memiliki rasa yang cenderung manis dan dikenal sebagai salah satu "
                "makanan khas Yogyakarta."
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
            "추천 메뉴가 무엇인가요?": "recommend"
        },

        "English": {
            "Hello": "hello",
            "One of these, please.": "one",
            "Thank you.": "thanks",
            "It's really delicious.": "delicious",
            "Please make it not spicy.": "not_spicy",
            "What do you recommend?": "recommend"
        },

        "Bahasa Indonesia": {
            "Halo": "hello",
            "Saya mau satu ini.": "one",
            "Terima kasih.": "thanks",
            "Sangat enak.": "delicious",
            "Tolong jangan terlalu pedas.": "not_spicy",
            "Menu apa yang Anda rekomendasikan?": "recommend"
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
                    r
                    for r in restaurants
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
# 맞춤 추천
# =========================================================
elif menu == f"✨ {t['recommend']}":

    st.title(
        f"✨ {t['recommend']}"
    )

    st.write(
        t["recommend_intro"]
    )

    spicy = st.radio(
        f"🌶 {t['spicy_question']}",
        [
            t["spicy_yes"],
            t["spicy_no"]
        ]
    )

    mood = st.selectbox(
        t["mood_question"],
        [
            t["traditional"],
            t["local_favorite"],
            t["quiet"]
        ]
    )

    if st.button(
        t["recommend_btn"],
        use_container_width=True
    ):

        if spicy == t["spicy_yes"]:
            r = restaurants[0]

        elif mood == t["local_favorite"]:
            r = restaurants[1]

        else:
            r = restaurants[2]

        st.success(
            f"✨ {t['recommend_success']}"
        )

        st.title(
            r["emoji"]
        )

        st.header(
            display_restaurant_name(r)
        )

        st.write(
            f"🍽 {display_food_name(r)}"
        )

        st.write(
            f"⭐ {r['rating']}"
        )

        st.write(
            f"📍 {r['region']}"
        )

        st.write(
            f"✨ {t[r['mood_key']]}"
        )


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
            