import json


def create_geojson_list(data_list):
    """
    Converts a list of data objects into a list of GeoJSON Point features.

    Args:
        data_list (list): List of data objects in dictionary format.

    Returns:
        dict: GeoJSON representation of the list of point features.
    """
    geojson_features = []

    for data in data_list:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [data["lng"], data["lat"]]
            },
            "properties": data
        }
        geojson_features.append(feature)

    # Create a FeatureCollection
    geojson_collection = {
        "type": "FeatureCollection",
        "features": geojson_features
    }

    return geojson_collection


# Read the JSON file with a list of data objects
with open('allProvinces.json', 'r', encoding="utf8") as file:
    data_list = json.load(file)

# Convert the list of data objects to GeoJSON
geojson_result = create_geojson_list(data_list)

# Save GeoJSON to a file
output_file_path = 'output.geojson'
with open(output_file_path, 'w', encoding="utf8") as output_file:
    json.dump(geojson_result, output_file, ensure_ascii=False, indent=2)

print(f"GeoJSON saved to {output_file_path}")
