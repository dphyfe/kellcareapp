import streamlit as st
import streamlit_folium

st.markdown("""
<style>
/* Make Streamlit main container wider */
.block-container {
	padding-left: 1.5rem !important;
	padding-right: 1.5rem !important;
	max-width: 98vw !important;
}

/* Flex container for map and cards */
.main-flex-row {
	display: flex;
	flex-direction: row;
	gap: 2rem;
	align-items: flex-start;
	width: 100%;
}
.map-container {
	width: 100%;
	min-width: 0;
	max-width: 100%;
	flex: 1 1 0;
}
.card-grid-container {
	flex: 3 1 0;
	width: 100%;
}
.card-grid {
	display: flex;
	flex-wrap: wrap;
	gap: 20px;
	justify-content: center;
	width: 100%;
	margin-left: 0 !important;
	margin-right: 0 !important;
	padding-left: 0 !important;
	padding-right: 0 !important;
}
</style>
""", unsafe_allow_html=True)


# --- COLUMN LAYOUT: MAP LEFT, CARDS RIGHT ---
col1, col2 = st.columns([1, 2])

with col1:
	st.title("Map of Your Location by Zipcode")
	zipcode = st.text_input("Enter your zipcode:")
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

				# Add a pin for each card's location
				card_locations = [
					(card["title"], card["location"]) for card in (
						[
							{"title": "The Laurels at Greentree Ridge", "location": "35.6160252, -82.3240143"},
							{"title": "Card 2", "location": "35.5951, -82.3515"},
							{"title": "Card 3", "location": "35.6000, -82.3550"},
							{"title": "Card 4", "location": "35.6100, -82.3400"},
							{"title": "Card 5", "location": "35.6200, -82.3200"},
							{"title": "Card 6", "location": "35.6250, -82.3300"},
						]
					)
				]
				for title, loc in card_locations:
					latlon = [float(x.strip()) for x in loc.split(",")]
					folium.Marker(latlon, popup=title, icon=folium.Icon(color="blue", icon="info-sign")).add_to(m)

				st_folium(m, width="100%", height=500)
			else:
				st.error("Could not find location for that zipcode.")
		except Exception as e:
			st.error(f"Error: {e}")

with col2:
	st.header("Image Card Grid with Hover Details")
	cards = [
		{"title": "The Laurels at Greentree Ridge", "img": "https://lh3.googleusercontent.com/p/AF1QipNMdg8lLBIb4Z1KSaHLb9-Xs6tSOl25SRLHht7d=s680-w680-h510-rw", "details": "Details for Card 1", "bar": "green", "price": "$1,200", "ratings": "4.5", "location": "35.6160252, -82.3240143"},
		{"title": "Card 2", "img": "https://placekitten.com/201/200", "details": "Details for Card 2", "bar": "red", "price": "$950", "ratings": "4.2", "location": "35.5951, -82.5515"},
		{"title": "Card 3", "img": "https://placekitten.com/202/200", "details": "Details for Card 3", "bar": "yellow", "price": "$1,050", "ratings": "4.0", "location": "35.6000, -82.5550"},
		{"title": "Card 4", "img": "https://placekitten.com/203/200", "details": "Details for Card 4", "bar": "green", "price": "$1,100", "ratings": "4.3", "location": "35.6100, -82.5300"},
		{"title": "Card 5", "img": "https://placekitten.com/204/200", "details": "Details for Card 5", "bar": "yellow", "price": "$1,250", "ratings": "4.6", "location": "35.6200, -82.5400"},
		{"title": "Card 6", "img": "https://placekitten.com/205/200", "details": "Details for Card 6", "bar": "red", "price": "$900", "ratings": "3.9", "location": "35.6250, -82.5200"},
		]
	
	
	st.markdown("""
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
		transition: transform 0.2s;
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
		background: rgba(0,0,0,0.7);
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
		opacity: 1;
	}
	.mock-bar {
		width: 80%;
		height: 16px;
		margin: 12px auto 0 auto;
		border-radius: 8px;
		background: #eee;
		overflow: hidden;
	}
	.mock-bar.green { background: #4caf50; }
	.mock-bar.red { background: #f44336; }
	.mock-bar.yellow { background: #ffeb3b; }
	</style>
	""", unsafe_allow_html=True)
	card_html = '<div class="card-grid">'
	for card in cards:
		card_html += f'<div class="card">'
		card_html += f'<img src="{card["img"]}" class="card-img" />'
		card_html += f'<div class="card-title">{card["title"]}</div>'
		card_html += f'<div class="card-details">{card["details"]}<br/>'
		card_html += f'<b>Price:</b> {card["price"] if "price" in card else "N/A"}<br/>'
		card_html += f'<b>Rating:</b> {card["ratings"] if "ratings" in card else "N/A"}<br/>'
		card_html += f'<div class="mock-bar {card["bar"]}"></div>'
		card_html += '</div>'  # close card-details
		card_html += '</div>'  # close card
	card_html += '</div>'
	st.markdown(card_html, unsafe_allow_html=True)
