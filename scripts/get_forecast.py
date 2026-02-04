#!/usr/bin/env python3
"""
Fetch weather forecast from National Weather Service API.
"""
import sys
import json
import argparse
import requests


def get_forecast(latitude, longitude):
    """
    Fetch weather forecast for given coordinates.

    Args:
        latitude: Latitude (decimal)
        longitude: Longitude (decimal)

    Returns:
        dict: Weather data including current conditions and forecast
    """
    try:
        # Step 1: Get grid point data
        points_url = f"https://api.weather.gov/points/{latitude},{longitude}"
        headers = {"User-Agent": "WeatherForecastSkill/1.0"}

        points_response = requests.get(points_url, headers=headers, timeout=10)
        points_response.raise_for_status()
        points_data = points_response.json()

        # Step 2: Get forecast URL
        forecast_url = points_data["properties"]["forecast"]
        forecast_hourly_url = points_data["properties"]["forecastHourly"]

        # Step 3: Fetch forecast
        forecast_response = requests.get(forecast_url, headers=headers, timeout=10)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()

        # Step 4: Fetch hourly forecast
        hourly_response = requests.get(forecast_hourly_url, headers=headers, timeout=10)
        hourly_response.raise_for_status()
        hourly_data = hourly_response.json()

        # Step 5: Check for alerts
        alerts_url = f"https://api.weather.gov/alerts/active?point={latitude},{longitude}"
        alerts_response = requests.get(alerts_url, headers=headers, timeout=10)
        alerts_response.raise_for_status()
        alerts_data = alerts_response.json()

        # Extract key information
        current_period = forecast_data["properties"]["periods"][0]

        result = {
            "location": {
                "lat": latitude,
                "lon": longitude,
                "city": points_data["properties"]["relativeLocation"]["properties"]["city"],
                "state": points_data["properties"]["relativeLocation"]["properties"]["state"]
            },
            "current": {
                "temperature": current_period["temperature"],
                "temperatureUnit": current_period["temperatureUnit"],
                "windSpeed": current_period["windSpeed"],
                "windDirection": current_period["windDirection"],
                "shortForecast": current_period["shortForecast"],
                "detailedForecast": current_period["detailedForecast"]
            },
            "forecast": {
                "periods": forecast_data["properties"]["periods"][:7]  # 7-day forecast
            },
            "hourly": {
                "periods": hourly_data["properties"]["periods"][:24]  # Next 24 hours
            },
            "alerts": [
                {
                    "event": alert["properties"]["event"],
                    "headline": alert["properties"]["headline"],
                    "severity": alert["properties"]["severity"],
                    "urgency": alert["properties"]["urgency"]
                }
                for alert in alerts_data.get("features", [])
            ]
        }

        return result

    except requests.HTTPError as e:
        if e.response.status_code == 404:
            return {
                "error": "Location not covered by National Weather Service. "
                         "This API only supports US territories."
            }
        return {"error": f"API error: {str(e)}"}

    except requests.RequestException as e:
        return {"error": f"Network error: {str(e)}"}

    except (KeyError, IndexError) as e:
        return {"error": f"Unexpected API response format: {str(e)}"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get weather forecast")
    parser.add_argument("--lat", type=float, required=True, help="Latitude")
    parser.add_argument("--lon", type=float, required=True, help="Longitude")

    args = parser.parse_args()

    result = get_forecast(args.lat, args.lon)
    print(json.dumps(result, indent=2))