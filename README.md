# GovGuide AI 🇮🇳

GovGuide AI is an AI-powered assistant built using Google's Agent Development Kit (ADK). It helps users discover Indian government scholarships and welfare schemes based on their personal details.

## Features

- Find government scholarships
- Recommend welfare schemes
- Supports Tamil and English
- Uses Google Gemini 3.5 Flash
- Uses ADK Tool Calling
- Reads scholarship data from a JSON knowledge base

## Technologies Used

- Python
- Google ADK
- Gemini 3.5 Flash
- JSON
- VS Code

## Project Structure

```
GovGuide_AI/
│── agent.py
│── tools.py
│── scholarships.json
│── __init__.py
│── README.md
│── .env
```

## How to Run

1. Install Google ADK
2. Add your Google API Key in `.env`
3. Run:

```bash
adk web
```

4. Open:

```
http://127.0.0.1:8000
```

## Example

User:

```
I am from Tamil Nadu.
I am studying AI & DS.
Family income is 2 lakh.
```

GovGuide AI recommends suitable scholarships and explains eligibility, benefits, documents, and application process.

## Author

Romanya R