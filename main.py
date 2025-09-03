import streamlit as st
import streamlit_folium
from streamlit_elements import elements

from st_clickable_images import clickable_images

from title import app_title
import title
from sidebar import Sidebar

from colors import MINT_BASE, MINT_DARK, MINT_DARKER, MINT_LIGHT, MINT_LIGHTER, MINT_DARKEST


Sidebar()

# Add About page link to sidebar


cards_data = [
    {
        "title": "The Laurels at Greentree Ridge",
        "img": "https://lh3.googleusercontent.com/p/AF1QipNMdg8lLBIb4Z1KSaHLb9-Xs6tSOl25SRLHht7d=s680-w680-h510-rw",
        "details": "Details for Card 1",
        "bar": "green",
        # "price": "$1,200",
        "ratings": "4.5",
        "location": "35.6160252, -82.3240143",
        "food_ratings": "4.1",
        "staff_ratings": "3.9",
        "atmosphere_ratings": "4.5",
        "cleanliness_ratings": "4.2",
        "safety_ratings": "3.8",
        "dogs_allowed": "true",
        "nursing_care_ratings": "4.7",
    },
    {
        "title": "North Carolina Veterans Home",
        "img": "https://lh3.googleusercontent.com/gps-cs-s/AC9h4nqPB2Q3vGcHAmQKd7hk7weg7ZD99Ru2QYyMDdzFwKj1UUdh78znKKYjJN_JrA-wwqFH97dxhjHgjCIlVx6TR5QZ_XxEIrf-lWbtI706CDBWFOxPj6m3KfHkj12JwffBdmC5gqO2=w408-h272-k-no",
        "details": "Details for Card 2",
        "bar": "red",
        # "price": "$950",
        "ratings": "4.2",
        "location": "35.5951, -82.3515",
        "food_ratings": "3.7",
        "staff_ratings": "4.2",
        "atmosphere_ratings": "4.0",
        "cleanliness_ratings": "3.8",
        "safety_ratings": "4.1",
        "dogs_allowed": "false",
        "nursing_care_ratings": "4.3",
    },
    {
        "title": "Swannanoa Valley Health and Rehabilitation",
        "img": "https://lh3.googleusercontent.com/p/AF1QipMyacgg_i4PymsystIyQDHQiSdR7uZqfnGKGQDU=w408-h306-k-no",
        "details": "Details for Card 3",
        "bar": "yellow",
        # "price": "$1,050",
        "ratings": "4.0",
        "location": "35.6000, -82.3550",
        "food_ratings": "4.3",
        "staff_ratings": "3.8",
        "atmosphere_ratings": "4.2",
        "cleanliness_ratings": "4.0",
        "safety_ratings": "3.9",
        "dogs_allowed": "true",
        "nursing_care_ratings": "4.5",
    },
    {
        "title": "Stonecreek Health and Rehabilitation",
        "img": "https://lh3.googleusercontent.com/p/AF1QipPNS1U5cYxqhbtmNn3vWF9cs5mRTuQB6ANlkgl2=w408-h272-k-no",
        "details": "Details for Card 4",
        "bar": "green",
        # "price": "$1,100",
        "ratings": "4.3",
        "location": "35.6100, -82.3300",
        "food_ratings": "4.0",
        "staff_ratings": "4.1",
        "atmosphere_ratings": "3.9",
        "cleanliness_ratings": "4.4",
        "safety_ratings": "4.2",
        "dogs_allowed": "false",
        "nursing_care_ratings": "4.6",
    },
    {
        "title": "Mountain Ridge Wellness Center",
        "img": "https://lh3.googleusercontent.com/gps-cs-s/AC9h4npxb-KMwen-EKTZSGo0rSAZQfCKVe3Cl4NBwWDSDsoFuyk8Yy82e3VapmUnQUeJhQQ9saSMFy4tg4CoKPypuVqQA6cOZq1BrkwWdFeWIUe0HExuP1RBuMW7utFwpb0zYKBGRgkc=w408-h725-k-no",
        "details": "Details for Card 5",
        "bar": "yellow",
        # "price": "$1,250",
        "ratings": "4.6",
        "location": "35.6200, -82.3300",
        "food_ratings": "3.9",
        "staff_ratings": "4.0",
        "atmosphere_ratings": "4.4",
        "cleanliness_ratings": "4.1",
        "safety_ratings": "4.3",
        "dogs_allowed": "true",
        "nursing_care_ratings": "4.8",
    },
    {
        "title": "Riverbend Health and Rehabilatation",
        "img": "https://lh3.googleusercontent.com/p/AF1QipNLnUNKscqOLiEEFPCIJlY3az7j5LOCxlx6r7Xk=w408-h270-k-no",
        "details": "Details for Card 6",
        "bar": "red",
        # "price": "$900",
        "ratings": "3.9",
        "location": "35.6250, -82.3200",
        "food_ratings": "4.2",
        "staff_ratings": "3.7",
        "atmosphere_ratings": "4.1",
        "cleanliness_ratings": "3.9",
        "safety_ratings": "4.0",
        "dogs_allowed": "false",
        "nursing_care_ratings": "4.4",
    },
]


features_object = {
    "food_ratings": "4.1",
    "staff_ratings": "3.9",
    "atmosphere_ratings": "4.5",
    "cleanliness_ratings": "4.2",
    "safety_ratings": "3.8",
    "dogs_allowed": "true",
    "nursing_care_ratings": "4.7",
}

st.markdown(
    f"""
<style>
/* Make Streamlit main container wider */
.block-container {{
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    max-width: 98vw !important;
}}

/* Flex container for map and cards_data */
.main-flex-row {{
    display: flex;
    flex-direction: row;
    gap: 2rem;
    align-items: flex-start;
    width: 100%;
}}
.map-container {{
    width: 100%;
    min-width: 0;
    max-width: 100%;
    flex: 1 1 0;
}}
.card-grid-container {{
    flex: 3 1 0;
    width: 100%;
}}
.card-grid {{
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
    width: 100%;
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
}}

/* Custom slider color: MINT_BASE */
div[data-baseweb="slider"] [class^="css-"][class*="-Rail"] {{
    background: {MINT_BASE} !important;
}}
div[data-baseweb="slider"] [class^="css-"][class*="-Track"] {{
    background: {MINT_BASE} !important;
}}
div[data-baseweb="slider"] [class^="css-"][class*="-Thumb"] {{
    background: {MINT_DARK} !important;
    border-color: {MINT_DARK} !important;
}}
</style>
<style>
/* Mint accent for buttons, checkboxes, radios, progress bars, links, focus, etc. */
/* Buttons */
button[kind], .stButton>button {{
    background-color: {MINT_DARKER} !important;
    border-color: {MINT_DARKER} !important;
}}
button[kind]:hover, .stButton>button:hover {{
    background-color: {MINT_DARKEST} !important;
    border-color: {MINT_DARKEST} !important;
}}
/* Checkbox and radio */
input[type="checkbox"]:checked + div, input[type="radio"]:checked + div {{
    background-color: {MINT_BASE} !important;
    border-color: {MINT_BASE} !important;
}}
/* Progress bar */
.stProgress > div > div > div > div {{
    background-color: {MINT_BASE} !important;
}}
/* Links */
a, .stMarkdown a {{
    color: {MINT_DARK} !important;
}}
a:hover, .stMarkdown a:hover {{
    color: {MINT_DARKER} !important;
}}
/* Focus ring */
*:focus {{
    outline-color: {MINT_BASE} !important;
}}
</style>
""",
    unsafe_allow_html=True,
)


col1, col2 = st.columns([1, 2])


def get_zipcodes_from_city(city, state_abbr="nc"):
    """
    Returns a list of zipcodes for a given city and state using the Zippopotam.us API.
    """
    import requests

    url = f"http://api.zippopotam.us/us/{state_abbr.lower()}/{city.lower().replace(' ', '%20')}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            zipcodes = [place["post code"] for place in data["places"]]
            return zipcodes
        else:
            return []
    except Exception:
        return []


with col1:
    app_title()
    st.title("Map of Your Location by Zipcode")
    zipcode = st.text_input("Enter your zipcode:")
    st.markdown("**Or enter a city and state to get a zipcode:**")
    city = st.text_input("City name")
    state_abbr = st.text_input("State abbreviation (e.g., NC)", value="NC")
    if city:
        zips = get_zipcodes_from_city(city, state_abbr)
        if zips:
            st.success(f"Zipcodes for {city.title()}, {state_abbr.upper()}: {', '.join(zips)}")
            # Optionally, auto-fill the zipcode input with the first result
            if not zipcode:
                zipcode = zips[0]
        else:
            st.error("No zipcodes found for that city and state.")

    selected_card_title = None
    if zipcode:
        import folium
        import requests
        from streamlit_folium import st_folium

        url = f"https://nominatim.openstreetmap.org/search?postalcode={zipcode}&country=USA&format=json"
        try:
            response = requests.get(url, headers={"User-Agent": "streamlit-app"})
            data = response.json()
            if data:
                lat = float(data[0]["lat"])
                lon = float(data[0]["lon"])
                st.success(f"Location found: {lat}, {lon}")
                m = folium.Map(location=[lat, lon], zoom_start=13)
                folium.Marker([lat, lon], popup=f"Zipcode: {zipcode}").add_to(m)

                # Add a pin for each card's location with unique popup (title)
                card_locations = [(card["title"], card["location"]) for card in cards_data]
                for title, loc in card_locations:
                    latlon = [float(x.strip()) for x in loc.split(",")]
                    folium.Marker(latlon, popup=title, icon=folium.Icon(color="blue", icon="info-sign")).add_to(m)

                # Use st_folium to get interaction data
                map_data = st_folium(m, width="100%", height=500)
                if map_data and map_data.get("last_object_clicked_popup"):
                    selected_card_title = map_data["last_object_clicked_popup"]
                    st.session_state["selected_card"] = selected_card_title
                elif "selected_card" in st.session_state:
                    selected_card_title = st.session_state["selected_card"]
            else:
                st.error("Could not find location for that zipcode.")
        except Exception as e:
            st.error(f"Error: {e}")


with col2:
    selected_card_title = st.session_state.get("selected_card", None)
    if st.session_state["show_high_ratings"]:
        cards_to_show = [card for card in cards_data if float(card.get("ratings", 0)) >= 4.3]
    else:
        cards_to_show = cards_data
    if selected_card_title:
        st.markdown(f"**Selected card:** {selected_card_title}")
        st.button("Show all cards_data", on_click=lambda: st.session_state.pop("selected_card", None))

    st.markdown(
        """
        <style>
        .card-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        .card {
            position: relative;
            width: 300px;
            height: 380px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            overflow: hidden;
            background: #fff;
            transition: transform 0.2s, border 0.2s;
            border: 3px solid transparent;
        }
        .card.selected {
            border: 3px solid {MINT_DARKER};
            box-shadow: 0 4px 16px {MINT_LIGHTER};
            z-index: 3;
        }
        .card:hover {
            transform: translateY(-8px) scale(1.03);
            z-index: 2;
        }
        .card-img {
            width: 100%;
            height: 100%;
            aspect-ratio: 1 / 1;
            object-fit: cover;
            position: absolute;
            top: 0;
            left: 0;
            z-index: 0;
        }
        .card-title {
            position: absolute;
            bottom: 0;
            width: 100%;
            z-index: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(0,0,0,0.35);
            color: #fff;
            text-align: center;
            padding: 8px 12px 8px 12px;
            font-size: 1.1em;
            font-weight: bold;
            transition: opacity 0.2s;
            opacity: 1;
        }
        .card:hover .card-title {
            opacity: 0;
        }
        .card-details {
            position: absolute;
            bottom: 0;
            width: 100%;
            z-index: 2;
            background: #fff;
            color: #222;
            text-align: center;
            padding: 16px 0 32px 0;
            font-size: 1em;
            opacity: 0;
            transition: opacity 0.2s;
            z-index: 1;
        }
        .card:hover .card-details {
            opacity: .73;
        }
        .mock-bar {
            width: 80%;
            height: 16px;
            margin: 12px auto 0 auto;
            border-radius: 8px;
            background: #eee;
            overflow: hidden;
        }
    .mock-bar.green { background: {MINT_DARK}; }
    .mock-bar.red { background: {MINT_DARKER}; }
    .mock-bar.yellow { background: {MINT_BASE}; }
        </style>
        """,
        unsafe_allow_html=True,
    )
    # Use clickable_images for all cards
    image_urls = [card["img"] for card in cards_to_show]
    titles = [card["title"] for card in cards_to_show]
    clicked_idx = clickable_images(image_urls, titles=titles, div_style={"display": "flex", "flex-wrap": "wrap", "gap": "20px", "justify-content": "center"}, img_style={"height": "220px", "width": "300px", "object-fit": "cover", "border-radius": "12px", "box-shadow": "0 2px 8px rgba(0,0,0,0.1)", "margin": "10px"})
    if "show_modal" not in st.session_state:
        st.session_state["show_modal"] = False
        st.session_state["modal_card"] = None

    # When a card is clicked, open the modal and set the card
    if clicked_idx > -1:
        st.session_state["show_modal"] = True
        st.session_state["modal_card"] = cards_to_show[clicked_idx]

    # ...existing code...

    # ...existing code...

    # Render modal if open
    if st.session_state.get("show_modal", False):
        card = st.session_state.get("modal_card", {})

        # Transparent button to close modal when clicking outside
        st.markdown(
            """
            <style>
            .modal-bg-btn {
                position: fixed;
                top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(0,0,0,0.45);
                border: none;
                z-index: 10000;
                cursor: pointer;
                padding: 0;
                margin: 0;
            }
            .modal-content {
                position: fixed;
                top: 50%; left: 50%;
                transform: translate(-50%, -50%);
                background: #fff;
                padding: 2rem 2.5rem;
                border-radius: 16px;
                box-shadow: 0 8px 32px rgba(0,0,0,0.18);
                max-width: 400px;
                width: 90vw;
                z-index: 10002;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Use a form to allow two buttons in a row
        with st.form("modal_form", clear_on_submit=True):
            # Invisible button as background
            close_bg = st.form_submit_button("", help="Click outside modal to close", use_container_width=True)
            # Modal content
            st.markdown(
                f"""
                <div class='modal-content'>
                    <img src='{card.get("img", "")}' style='width:100%;border-radius:12px;margin-bottom:1rem;' />
                    <h3 style='margin:0 0 0.5rem 0;'>{card.get("title", "")}</h3>
                    <div style='margin-bottom:0.5rem;'>{card.get("details", "")}</div>
                    <b>Rating:</b> {card.get("ratings", "N/A")}<br/>
                    <b>Dogs Allowed:</b> {("Yes" if str(card.get("dogs_allowed", "")).lower() == "true" else "No")}<br/>
                    <b>Atmosphere:</b> {card.get("atmosphere_ratings", "N/A")}<br/>
                    <b>Cleanliness:</b> {card.get("cleanliness_ratings", "N/A")}<br/>
                    <b>Safety:</b> {card.get("safety_ratings", "N/A")}<br/>
                    <b>Nursing Care:</b> {card.get("nursing_care_ratings", "N/A")}<br/>
                    <br/>
                    <button type="submit" name="close_modal" style="margin-top:1rem;background:{MINT_DARKER};color:#fff;padding:0.5rem 1.5rem;border:none;border-radius:8px;cursor:pointer;">Close Modal Card</button>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if close_bg:
                st.session_state["show_modal"] = False
                st.session_state["modal_card"] = None
