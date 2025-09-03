import streamlit as st

from colors import MINT_BASE, MINT_DARK, MINT_DARKER, MINT_DARKEST


class Sidebar:
    def __init__(self):
        # Sidebar title at the very top
        from title import sidebar_title

        sidebar_title(title="Kellcare Help Desk")

        # Ratings filter buttons at the very top of the sidebar
        if "show_high_ratings" not in st.session_state:
            st.session_state["show_high_ratings"] = False
        if st.sidebar.button("Show only 4.3+ ratings", key="show_high_ratings_btn"):
            st.session_state["show_high_ratings"] = True
        if st.sidebar.button("Show all ratings", key="show_all_ratings_btn"):
            st.session_state["show_high_ratings"] = False

        self.show_testimonials()
        self.show_five_star_reviews()
        self.show_friendliness_slider()
        self.show_ratings_sliders()
        self.show_dogs_allowed()

        # Inject CSS to make only sidebar sliders and buttons use MINT_DARKEST
        st.sidebar.markdown(
            f"""
            <style>
            /* Sidebar slider track, rail, thumb, and text use mint palette */
            section[data-testid='stSidebar'] div[data-baseweb='slider'] [class*='Track'],
            section[data-testid='stSidebar'] div[data-baseweb='slider'] [class*='Rail'] {{
                background: {MINT_BASE} !important;
            }}
            section[data-testid='stSidebar'] div[data-baseweb='slider'] [class*='Thumb'],
            section[data-testid='stSidebar'] div[data-baseweb='slider'] [role='slider'] {{
                background: {MINT_DARKER} !important;
                border-color: {MINT_DARKER} !important;
                box-shadow: 0 0 2px {MINT_DARKER}, 0 0 4px {MINT_DARKER};
            }}
            /* Slider value text and label */
            section[data-testid='stSidebar'] .css-1c7y2kd, /* value */
            section[data-testid='stSidebar'] .css-1y4p8pa, /* label */
            section[data-testid='stSidebar'] label {{
                color: {MINT_DARKEST} !important;
            }}
            /* Make all sidebar buttons mint darkest */
            section[data-testid='stSidebar'] button {{
                background-color: {MINT_DARKEST} !important;
                border-color: {MINT_DARKEST} !important;
                color: #fff !important;
            }}
            section[data-testid='stSidebar'] button:hover {{
                background-color: {MINT_DARKEST} !important;
                border-color: {MINT_DARKEST} !important;
                filter: brightness(1.1);
            }}
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

    # Remove class-level checkbox, move to __init__

    def show_dogs_allowed(self):
        dogs_allowed = st.sidebar.checkbox("", value=True)
        dogs_allowed_display = "🐶" if dogs_allowed else "❌"
        st.sidebar.write(f"Dogs Allowed: {dogs_allowed_display}")

    # Call in __init__
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
