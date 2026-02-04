#!/usr/bin/env python3
"""
Geocode city names to coordinates using Nominatim OpenStreetMap API.
"""
import sys
import json
import requests


def geocode_city(city_name):
    """
    Convert city name to coordinates.

    Args:
        city_name: City name (e.g., "New York, NY" or "Seattle")

    Returns:
        dict: {"lat": float, "lon": float, "display_name": str}
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city_name,
        "format": "json",
        "limit": 1,
        "countrycodes": "us"  # Limit to US since NWS is US-only
    }
    headers = {
        "User-Agent": "WeatherForecastSkill/1.0"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()

        results = response.json()
        if not results:
            return {"error": f"City not found: {city_name}"}

        location = results[0]
        return {
            "lat": float(location["lat"]),
            "lon": float(location["lon"]),
            "display_name": location["display_name"]
        }

    except requests.RequestException as e:
        return {"error": f"Geocoding failed: {str(e)}"}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: geocode.py <city name>"}))
        sys.exit(1)

    city = " ".join(sys.argv[1:])
    result = geocode_city(city)
    print(json.dumps(result, indent=2))
