import streamlit as st


def app_title():
    st.markdown(
        """
		<h1 style='text-align: center; color: #1976d2; margin-bottom: 0.5em;'>KellCare Nursing Home Finder</h1>
		<h4 style='text-align: center; color: #444; margin-top: 0;'>Find the best care facilities near you</h4>
	""",
        unsafe_allow_html=True,
    )


def sidebar_title(title: str, subtitle: str = None):
    st.sidebar.markdown(f"<h2 style='color: #1976d2; margin-bottom: 0.2em;'>{title}</h2>", unsafe_allow_html=True)
    if subtitle:
        st.sidebar.markdown(f"<h5 style='color: #444; margin-top: 0;'>{subtitle}</h5>", unsafe_allow_html=True)


print("hello")
pick_animal_options = ["Dog", "Cat", "Bird", "turtle"]
picker_options = ["$", "$$", "$$$"]
