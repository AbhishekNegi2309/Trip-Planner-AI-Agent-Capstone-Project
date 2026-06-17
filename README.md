# 🌍 Trip Planner AI Agent

An AI-powered travel itinerary generator built with **Streamlit + OpenAI Agents + external location APIs**.

The system generates personalized multi-day travel itineraries using LLM reasoning, POI search, and optional map-based context.

---

## 🚀 Features

- ✈️ AI-generated travel itineraries (day-by-day plans)
- 🧠 OpenAI-powered agent reasoning (tool calling enabled)
- 📍 POI search integration (OpenStreetMap / Overpass API)
- 🗺️ Map-based visualization of destinations
- 💬 Feedback loop for itinerary improvement
- ⚡ Fast Streamlit UI for interactive planning

---

## 🧱 Architecture
User Input → Streamlit UI → Planner Agent → OpenAI (Tool Calling)
↓
POI Search / Wiki RAG / APIs
↓
Structured Itinerary Output

---

## 📦 Tech Stack

- Python
- Streamlit
- OpenAI API (Responses + Tool Calling)
- OpenStreetMap / Nominatim API
- Overpass API
- Pandas / Requests

---

## 📁 Project Structure

agents/ → AI planning logic
tools/ → POI search, RAG, feedback
services/ → API integrations
ui/ → Streamlit UI components
utils/ → helpers, validation, cache
data/ → app state + feedback logs

```
trip-planner-ai-agent/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── agents/
│   ├── planner_agent.py
│   └── schemas.py
│
├── tools/
│   ├── poi_search.py
│   ├── wikivoyage_rag.py
│   └── feedback.py
│
├── services/
│   ├── openai_service.py
│   ├── nominatim.py
│   └── overpass.py
│
├── ui/
│   ├── itinerary_view.py
│   └── map_view.py
│
├── utils/
│   ├── helpers.py
│   ├── cache.py
│   └── validation.py
│
└── data/
    ├── app_state.json
    └── feedback.jsonl
```
---

## ⚙️ Setup Instructions

### 1. Clone repository
```bash
git clone https://github.com/your-username/trip-planner-ai-agent.git
cd trip-planner-ai-agent
```

## Create virtual environment

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

## Install dependencies

pip install -r requirements.txt

## Add environment variables

OPENAI_API_KEY=your_api_key_here

## Run Streamlit app

streamlit run app.py

## 📄 License

This project is licensed under the MIT License.


👨‍💻 Author

Built by Abhishek Negi
