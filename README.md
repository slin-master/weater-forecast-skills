# Weather Forecast Agent Skill

> Real-time weather forecasts for US locations using the National Weather Service API.

A lightweight [Agent Skill](https://agentskills.io/) that enables Claude and other AI agents to fetch current conditions, 7-day forecasts, and active weather alerts for any US location.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Agent Skills Compatible](https://img.shields.io/badge/Agent_Skills-Compatible-blue.svg)](https://agentskills.io/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Features

- ✅ **Current conditions**: Temperature, wind speed, humidity
- ✅ **7-day forecast**: Daily summaries with highs/lows
- ✅ **Weather alerts**: Active warnings and watches
- ✅ **Hourly forecast**: Hour-by-hour predictions for next 24h
- ✅ **No API key required**: Uses free National Weather Service API
- ✅ **Geocoding included**: Convert city names to coordinates automatically

## Quick Start

### Installation

#### Option 1: Using UV (Recommended)

Install UV if you haven't already
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Clone to your skills directory
```bash
git clone https://github.com/slin-master/weather-forecast-skills.git ~/.claude/skills/weather-forecast
```
Dependencies are installed automatically when running scripts via `uv run`

#### Option 2: Using pip

Clone to your skills directory
```bash
git clone https://github.com/slin-master/weather-forecast-skills.git ~/.claude/skills/weather-forecast
```

Install dependencies
```sh
cd ~/.claude/skills/weather-forecast
pip install -e .
```

### Usage with Claude Code

1. Restart Claude Code to detect the new skill
2. Ask: _"What's the weather in Seattle?"_
3. Claude will automatically use this skill to fetch real-time data

### Usage with VS Code Copilot

1. Enable Agent Skills in VS Code settings: `chat.useAgentSkills`
2. Restart VS Code
3. In Copilot Chat, ask about weather for any US city

## How It Works

This skill follows the [Agent Skills specification](https://agentskills.io/):

```
weather-forecast/
├── SKILL.md              # Skill definition and instructions
├── scripts/
│   ├── geocode.py        # Convert city names to coordinates
│   └── get_forecast.py   # Fetch weather from NWS API
├── references/
│   └── NWS_API.md        # API documentation
└── requirements.txt      # Python dependencies
```

When Claude detects a weather-related query:
1. Loads `SKILL.md` instructions
2. Runs `geocode.py` to get coordinates (if needed)
3. Executes `get_forecast.py` with those coordinates
4. Presents results in natural language

## Testing Scripts Standalone

The Python scripts work independently for testing:

#### With UV (Recommended):

Test geocoding
```bash
uv run scripts/geocode.py "Portland, OR"
```
Test weather forecast
```bash
uv run scripts/get_forecast.py --lat 45.5152 --lon -122.6784
```

#### With pip:

Test geocoding
```bash
python scripts/geocode.py "Portland, OR"
```

Test weather forecast
```bash
python scripts/get_forecast.py --lat 45.5152 --lon -122.6784
```

## Example Interactions

**User**: _"What's the weather like in San Francisco today?"_

**Claude** (using this skill):
> In San Francisco, it's currently 58°F and partly cloudy. Expect a high of 65°F today with winds from the west at 12 mph. No precipitation expected.

**User**: _"Will it rain in Chicago this week?"_

**Claude** (using this skill):
> Looking at Chicago's 7-day forecast, rain is likely on Thursday (75% chance, 0.5-1 inch) and Saturday afternoon (60% chance). The rest of the week should be dry with partly cloudy skies.

## Supported Platforms

- ✅ [Claude Code](https://claude.ai/download)
- ✅ [VS Code with GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- ✅ [Cursor](https://cursor.sh/)
- ✅ Claude API (via Skills SDK)

## API Coverage

This skill uses the [National Weather Service API](https://www.weather.gov/documentation/services-web-api), which covers:
- 🇺🇸 All US states and territories
- 🇵🇷 Puerto Rico, US Virgin Islands
- 🇬🇺 Guam, American Samoa

**Note**: For international weather, consider extending this skill with additional APIs like OpenWeatherMap or WeatherAPI.

## Learn More

📖 **Read the full tutorial**: [Building Your First Agent Skill](https://friedrichs-it.de/blog/building-agent-skills-tutorial)

This README accompanies a comprehensive hands-on tutorial that walks through:
- Creating Agent Skills from scratch
- Best practices for SKILL.md structure
- Comparing Agent Skills vs MCP servers
- Advanced patterns and deployment strategies

## Requirements

- Python 3.8+
- [UV](https://docs.astral.sh/uv/) (recommended) or pip
- Dependencies: See `pyproject.toml`

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contributions

- [ ] Add international weather API support
- [ ] Implement caching to reduce API calls
- [ ] Generate weather visualizations (charts/maps)
- [ ] Add air quality index integration
- [ ] Support weather alerts notifications

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Attribution

Created by [Nils Friedrichs](https://friedrichs-it.de) as part of the Agent Skills ecosystem.

Based on data from:
- [National Weather Service API](https://www.weather.gov/documentation/services-web-api)
- [Nominatim (OpenStreetMap)](https://nominatim.org/)

## Related Projects

- [Agent Skills Specification](https://agentskills.io/)
- [Anthropic Skills Repository](https://github.com/anthropics/skills)
- [MCP Servers Registry](https://www.lightnow.ai/servers) - For comparing to MCP approach

---

**Questions or feedback?** [Open an issue](https://github.com/slin-master/weather-forecast-skills/issues) or [contact me](https://friedrichs-it.de/contact).
