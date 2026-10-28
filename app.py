            st.info(t["research_note"])
        else:
            st.info(t["unknown"])
    st.divider()
    st.subheader(f'📍 {t["map"]}')
    for r in food_restaurants[:20]:
        st.write(f'{r["emoji"]} **{display_restaurant(r)}** · {display_location(r)} · {display_price(r)}')

# ---------------------------------------------------------
# 지역 언어 번역 / 발음
# ---------------------------------------------------------
elif menu == f'💬 {t["language"]}':
    st.title(f'💬 {t["language"]}')
    st.write(t["translation_intro"])
    phrase_names = [p["id"] for p in PHRASES]
    selected_phrase = st.selectbox(t["phrase"], phrase_names)
    p = next(x for x in PHRASES if x["id"] == selected_phrase)
    c1, c2, c3 = st.columns(3)
    c1.metric("🇮🇩 Bahasa Indonesia", p["id"])
    c2.metric("🇰🇷 한국어", p["ko"])
    c3.metric("🇺🇸 English", p["en"])
    st.info(f'🗣️ **{t["pronunciation"]}:** {p["pron"]}')
    st.caption(p["meaning"])
    st.divider()
    st.subheader("🍽️ 음식점과 지역 언어")
    language_restaurant_name = st.selectbox(
        t["restaurant_name"],
        [r["name"] for r in all_restaurants],
        format_func=lambda n: display_restaurant(next(r for r in all_restaurants if r["name"] == n)),
        key="language_restaurant_select"
    )
    language_restaurant = next(r for r in all_restaurants if r["name"] == language_restaurant_name)
    st.write(f'**{t["cuisine"]}:** {language_restaurant.get("cuisine", display_food(language_restaurant))}')
    st.write(f'**{t["address"]}:** {display_location(language_restaurant)}')
    if language_restaurant.get("local_language"):
        st.write(f'**{t["local_language"]}:** {language_restaurant["local_language"]}')
    if language_restaurant.get("data_source") == "local_research":
        st.caption(t["research_note"])
    else:
        info = FOOD_INFO.get(language_restaurant["food"])
        if info:
            st.caption(info.get("id", ""))

# ---------------------------------------------------------
# 리뷰 · 커뮤니티
# ---------------------------------------------------------
elif menu == f'⭐ {t["review"]}':
    st.title(f'⭐ {t["review"]}')
    st.write(t["intro"])
    with st.form("review_form", clear_on_submit=True):
        restaurant_names = [r["name"] for r in all_restaurants]
        selected_review_restaurant = st.selectbox(t["visited"], restaurant_names,
            format_func=lambda n: display_restaurant(next(r for r in all_restaurants if r["name"] == n)))
        overall = st.slider(t["stars"], 1, 5, 5)
        c1, c2, c3 = st.columns(3)
        taste = c1.slider(t["taste"], 1, 5, 5)
        value = c2.slider(t["value"], 1, 5, 4)
        service = c3.slider(t["service"], 1, 5, 5)
        culture = st.checkbox(t["culture_check"])
        hidden = st.checkbox(t["hidden_check"])
        phrase = st.text_input(t["local_phrase"])
        review_text = st.text_area(t["review_text"])
        uploaded_photo = st.file_uploader(t["photo"], type=["png", "jpg", "jpeg"])
        review_submit = st.form_submit_button(t["submit"])
    if review_submit:
        photo_bytes = uploaded_photo.getvalue() if uploaded_photo is not None else None
        st.session_state.reviews.append({
            "restaurant": selected_review_restaurant, "rating": overall, "taste": taste,
            "value": value, "service": service, "culture": culture, "hidden": hidden,
            "phrase": phrase.strip(), "review": review_text.strip(),
            "photo_bytes": photo_bytes, "photo_name": uploaded_photo.name if uploaded_photo else None
        })
        st.session_state.points += 50
        st.success(t["review_success"])
        st.caption(t["upload_note"])
    st.divider()
    st.subheader(t["recent_reviews"])
    if not st.session_state.reviews:
        st.info(t["no_reviews"])
    else:
        for item in reversed(st.session_state.reviews):
            match = next((r for r in all_restaurants if r["name"] == item["restaurant"]), None)
            title = display_restaurant(match) if match else item["restaurant"]
            with st.container(border=True):
                st.write(f'**{title}** · {"⭐" * item["rating"]}')
                if item.get("review"):
                    st.write(item["review"])
                st.caption(f'{t["taste"]}: {item["taste"]}/5 · {t["value"]}: {item["value"]}/5 · {t["service"]}: {item["service"]}/5')
                tags = []
                if item.get("culture"): tags.append(t["culture_review"])
                if item.get("hidden"): tags.append(t["hidden_check"])
                if tags: st.caption(" · ".join(tags))
                if item.get("phrase"): st.info(f'{t["local_phrase"]}: {item["phrase"]}')
                if item.get("photo_bytes"): st.image(item["photo_bytes"], caption=item.get("photo_name", "Food photo"), use_container_width=True)

# ---------------------------------------------------------
# 맞춤 추천
# ---------------------------------------------------------
elif menu == f'✨ {t["recommend"]}':
    st.title(f'✨ {t["recommend"]}')
    st.write(t["recommend_intro"])
    c1, c2 = st.columns(2)
    spicy_choice = c1.selectbox(t["spicy"], [t["all"], "🌶️ 매운 음식", "🌿 맵지 않은 음식"])
    budget_choice = c2.selectbox(t["price_filter"], [t["all"], t["budget"], t["mid"], t["high"]])
    category_labels = [t["all"]] + list(CATEGORY_NAMES.values())
    category_choice = st.selectbox(t["food_type"], category_labels)
    areas = [t["all"]] + sorted(set(region_name(r) for r in all_restaurants))
    area_choice = st.selectbox(t["region"], areas)
    all_tags = sorted(set(tag for r in all_restaurants for tag in r.get("tags", [])))
    tag_choice = st.selectbox(t["tag"], [t["all"]] + all_tags)
    use_favorites = st.checkbox(t["use_favorites"])
    if st.button(t["recommend_btn"], use_container_width=True):
        scored = []
        for r in all_restaurants:
            score, reasons = 0.0, []
            rating = current_rating(r)
            # 실제 이용자 리뷰가 있을 때만 평점을 추천 점수에 반영합니다.
            if rating is not None and reviews_for(r["name"]):
                score += rating / 5
                reasons.append(f'⭐ {rating:.1f}')
            if spicy_choice == "🌶️ 매운 음식":
                if r.get("spicy") is True:
                    score += 2; reasons.append("🌶️")
                elif r.get("spicy") is False:
                    score -= 1
            elif spicy_choice == "🌿 맵지 않은 음식":
                if r.get("spicy") is False:
                    score += 2; reasons.append("🌿")
                elif r.get("spicy") is True:
                    score -= 1
            if budget_choice != t["all"] and price_match(r, budget_choice):
                score += 1; reasons.append(t["price_filter"])
            if category_choice != t["all"] and category_display(r) == category_choice:
                score += 3; reasons.append(category_choice)
            if area_choice != t["all"] and region_name(r) == area_choice:
                score += 2; reasons.append(area_choice)
            if tag_choice != t["all"] and tag_choice in r.get("tags", []):
                score += 2; reasons.append(tag_choice)
            if use_favorites and any(x in r["food"] or x in r.get("food_ko","") for x in st.session_state.favorites):
                score += 2; reasons.append(t["favorites"])
            scored.append((score, reasons, r))
        scored.sort(key=lambda x: x[0], reverse=True)
        st.success(t["recommend_btn"])
        for rank, (score, reasons, r) in enumerate(scored[:3], 1):
            with st.container(border=True):
                st.subheader(f'{rank}. {r["emoji"]} {display_restaurant(r)}')
                st.write(f'{display_food(r)} · {display_location(r)} · {display_price(r)}')
                st.write(f'⭐ {rating_text(r)} · 💬 {review_count(r)}')
                st.info(f'{t["why"]}: ' + (" · ".join(reasons) if reasons else t["research_data"]))
                add_favorite_button(r, f"recommend_{rank}")

# ---------------------------------------------------------
# 음식 카테고리 탐색
# ---------------------------------------------------------
elif menu == f'🍽 {t["categories"]}':
    st.title(f'🍽 {t["categories"]}')
    st.write(t["intro"])
    chosen_category = st.selectbox(t["category"], list(CATEGORY_NAMES.values()))
    chosen_area = st.selectbox(t["region"], [t["all"]] + sorted(set(region_name(r) for r in all_restaurants)))
    chosen_budget = st.selectbox(t["price_filter"], [t["all"], t["budget"], t["mid"], t["high"]])
