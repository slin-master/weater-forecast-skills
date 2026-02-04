# National Weather Service API Reference

## Endpoints

### Points API
`GET /points/{lat},{lon}`

Returns metadata about a location, including:
- Grid coordinates for forecast URLs
- Time zone
- Radar station
- Forecast office

### Forecast API
`GET /gridpoints/{office}/{gridX},{gridY}/forecast`

Returns 7-day forecast with:
- Day/night periods
- Temperature and wind
- Detailed text forecast

### Alerts API
`GET /alerts/active?point={lat},{lon}`

Returns active weather alerts:
- Warnings (severe conditions)
- Watches (conditions possible)
- Advisories (less urgent)

## Rate Limits

- No API key required
- Please use a descriptive User-Agent
- Recommended: 1 request per second