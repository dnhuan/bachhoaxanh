import folium
import json

# Load the GeoJSON data from the saved file
with open('output.geojson', 'r', encoding="utf8") as file:
    geojson_data = json.load(file)

# Create a Folium map centered around Vietnam
vietnam_center = [14.0583, 108.2772]  # Latitude and longitude of Vietnam's center
m = folium.Map(location=vietnam_center, zoom_start=6)

# Add GeoJSON data to the map
folium.GeoJson(
    geojson_data,
    name='geojson_data'
).add_to(m)

# Save the map to an HTML file
output_map_path = 'output_map.html'
m.save(output_map_path)

print(f"Map saved to {output_map_path}. Open the HTML file in a web browser to view the map.")
