---
title: CultureBot
emoji: 🌍
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.45.1
app_file: app.py
pinned: false
license: mit
---

# CultureBot 🌍

CultureBot is an AI-powered Streamlit application that helps users learn about world cultures through interactive conversations and curated cultural facts.

## Features

- **AI-Powered Chat**: Ask questions about any culture or country and get intelligent responses
- **Cultural Facts Database**: Browse curated cultural insights from around the world
- **Interactive Interface**: Beautiful, responsive design with multiple pages
- **Global Coverage**: Information about customs, traditions, and practices from various countries

## How to Use

1. **Home Page**: Get an overview of CultureBot's features
2. **Chat**: Interact with the AI assistant about cultural topics
3. **Cultural Facts**: Browse facts by country or category
4. **About**: Learn more about the application and its mission

## Setup for Local Development

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your OpenAI API key:
   - Create a `.streamlit/secrets.toml` file
   - Add your API key: `openai_api_key = "your-api-key-here"`
4. Run the app: `streamlit run app.py`

## Deployment on Hugging Face Spaces

This application is optimized for deployment on Hugging Face Spaces. To deploy:

1. Create a new Space on Hugging Face
2. Choose Streamlit as the SDK
3. Upload the files from this repository
4. Add your OpenAI API key in the Space settings under "Repository secrets"
   - Key: `OPENAI_API_KEY`
   - Value: Your OpenAI API key

## Technologies Used

- **Streamlit**: Web application framework
- **OpenAI GPT-3.5**: AI language model for intelligent responses
- **Python**: Programming language
- **Hugging Face Spaces**: Deployment platform

## Cultural Coverage

The application includes cultural facts and insights from:
- Japan
- India
- Brazil
- Germany
- China
- France
- South Korea
- Mexico
- Egypt
- Russia
- Thailand
- Italy

## Contributing

We welcome contributions to expand our cultural database and improve the application. Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License.