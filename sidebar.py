import streamlit as st
import title


title.sidebar_title(title="Kellcare Help Desk")


class Sidebar:
    def __init__(self):
        self.show_testimonials()
        self.show_five_star_reviews()
        self.show_friendliness_slider()
        self.show_ratings_sliders()

        # Inject CSS to make only sidebar sliders pink
        st.sidebar.markdown(
            """
            <style>
            /* Make only sidebar sliders pink */
            section[data-testid="stSidebar"] div[data-baseweb="slider"] [class*="Track"],
            section[data-testid="stSidebar"] div[data-baseweb="slider"] [class*="Rail"],
            section[data-testid="stSidebar"] div[data-baseweb="slider"] [class*="Thumb"],
            section[data-testid="stSidebar"] div[data-baseweb="slider"] [role="slider"] {
                background: #ff0099 !important;
                border-color: #ff0099 !important;
                box-shadow: 0 0 2px #ff0099, 0 0 4px #ff0099;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

    def show_ratings_sliders(self):
        st.sidebar.markdown("---")
        st.sidebar.markdown("### Rate Facility Features")
        food = st.sidebar.slider("Food Quality", min_value=1.0, max_value=5.0, value=4.0, step=0.1)
        staff = st.sidebar.slider("Staff Friendliness", min_value=1.0, max_value=5.0, value=4.0, step=0.1)
        atmosphere = st.sidebar.slider("Atmosphere", min_value=1.0, max_value=5.0, value=4.0, step=0.1)
        cleanliness = st.sidebar.slider("Cleanliness", min_value=1.0, max_value=5.0, value=4.0, step=0.1)
        safety = st.sidebar.slider("Safety", min_value=1.0, max_value=5.0, value=4.0, step=0.1)
        nursing = st.sidebar.slider("Nursing Care", min_value=1.0, max_value=5.0, value=4.0, step=0.1)

    dogs_allowed = st.sidebar.checkbox("Dogs Allowed (check for 🐶, uncheck for ❌)", value=True)
    dogs_allowed_display = "🐶" if dogs_allowed else "❌"
    # st.sidebar.write(f"**Your Ratings:**\n- Food: {food}\n- Staff: {staff}\n- Atmosphere: {atmospshere}\n- Cleanliness: {cleanliness}\n- Safety: {safety}\n- Nursing Care: {nursing}\n- Dogs Allowed: {dogs_allowed_display}")

    def show_testimonials(self):
        if st.sidebar.button("Testimonials"):
            st.sidebar.info("⭐️ 'This service was amazing!' - Jane D.\n\n⭐️ 'Helped my family so much.' - Mark T.")

    def show_five_star_reviews(self):
        if st.sidebar.button("5 Star Reviews"):
            st.sidebar.info("🌟 'Absolutely perfect care!' - Alice W.\n\n🌟 'Could not ask for better.' - Bob S.")

    def show_friendliness_slider(self):
        if "show_friendliness_slider" not in st.session_state:
            st.session_state["show_friendliness_slider"] = False

        if st.sidebar.button("Rate Friendliness"):
            st.session_state["show_friendliness_slider"] = True

        if st.session_state["show_friendliness_slider"]:
            friendliness = st.sidebar.slider("Friendliness", min_value=1, max_value=5, value=3)
            st.sidebar.write(f"Friendliness rating: {friendliness} ⭐")
