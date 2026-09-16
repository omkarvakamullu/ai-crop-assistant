# 🌾 AI Crop Process Explainer Bot

A Generative AI chatbot that explains crop lifecycle and farming processes — sowing, irrigation, harvesting, and storage — in simple, farmer-friendly language.

## Overview

This project integrates Google's Gemini Flash model with Python and Streamlit to build an interactive AI-powered web application. Users can ask natural language questions about crop processes and receive clear, simplified answers.

## Features

- Interactive chat-style interface built with Streamlit
- Powered by Gemini Flash for fast, lightweight AI responses
- Custom system prompt design to keep responses accurate, on-topic, and easy to understand
- Covers key crop lifecycle stages: sowing, irrigation, harvesting, and storage

## Tech Stack

- **Python** — core application logic
- **Google Gemini Flash API** — AI model for generating responses
- **Streamlit** — web interface
- **python-dotenv** — secure API key management

## How It Works

1. User submits a question through the Streamlit interface
2. The app attaches a system prompt instructing the AI to act as a farming assistant
3. The combined message is sent to Gemini Flash via an API call
4. The AI-generated response is extracted and displayed back to the user

## Setup

1. Clone this repository
2. Install dependencies:
```bash
   pip install requests python-dotenv streamlit
```
3. Create a `.env` file in the project root with your Gemini API key: