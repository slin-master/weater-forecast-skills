---
name: weather-forecast
description: Fetch real-time weather forecasts for US locations using the National Weather Service API. Use when the user asks about weather, temperature, or conditions for a specific US city or coordinates.
license: MIT
metadata:
  author: Nils Friedrichs
  version: "1.0.0"
  capabilities:
    - weather-data
    - temperature-alerts
    - forecast-summary
---

# Weather Forecast Skill

This skill provides access to real-time weather data from the National Weather Service (NWS) API.

## Capabilities

- **Current conditions**: Temperature, humidity, wind speed
- **7-day forecast**: Daily summaries with high/low temperatures
- **Weather alerts**: Active warnings and watches
- **Hourly forecast**: Detailed hour-by-hour predictions

## Usage

When the user asks about weather, follow this workflow:

1. **Get coordinates**: 
   - If the user provides a city name, use the geocoding script to get lat/lon
   - If they provide coordinates directly, use those

2. **Fetch forecast**:
   - Run `scripts/get_forecast.py --lat <latitude> --lon <longitude>`
   - The script returns JSON with forecast data

3. **Present results**:
   - Summarize the current conditions clearly
   - Include the 7-day forecast if requested
   - Highlight any active weather alerts

## Scripts

### `scripts/get_forecast.py`

Fetches weather data from NWS API. Requires latitude and longitude.

**Usage**:
```bash
python scripts/get_forecast.py --lat 40.7128 --lon -74.0060
```

**Output**: JSON with current conditions and forecast

### `scripts/geocode.py`

Converts city names to coordinates using Nominatim OpenStreetMap API.

**Usage**:
```bash
python scripts/geocode.py "New York, NY"
```

**Output**: JSON with latitude and longitude

## Error Handling

- **Invalid coordinates**: NWS API only covers US territories. Return helpful message if coordinates are outside coverage.
- **API errors**: If API is down, inform user and suggest trying again later.
- **Missing city**: If geocoding fails, ask user for coordinates directly.

## Examples

**User**: "What's the weather in Seattle?"

**Response**:
1. Geocode "Seattle, WA" → lat: 47.6062, lon: -122.3321
2. Fetch forecast for those coordinates
3. Present: "In Seattle, it's currently 52°F and partly cloudy. High of 58°F today with a 30% chance of rain this evening."

**User**: "Will it rain in Chicago this week?"

**Response**:
1. Geocode "Chicago, IL"
2. Fetch 7-day forecast
3. Analyze precipitation chances
4. Present: "Looking at Chicago's 7-day forecast, rain is likely on Thursday (80% chance) and Saturday (60% chance). The rest of the week looks clear."