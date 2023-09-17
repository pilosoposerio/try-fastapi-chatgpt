# FastAPI ChatGPT Sample Project

This repository contains a sample project that demonstrates how to integrate [FastAPI](https://fastapi.tiangolo.com/) with ChatGPT, a powerful language model developed by OpenAI. With this project, you can create a simple web application that allows users to interact with ChatGPT through a RESTful API.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.8+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [OpenAI GPT-3 Python Client](https://github.com/openai/openai-python)
- An OpenAI API key (Sign up at [OpenAI](https://beta.openai.com/signup/) and follow their API key setup instructions)

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/pilosoposerio/try-fastapi-chatgpt.git
   cd fastapi-chatgpt-sample
   ```

1. Create a Python virtual environment:

   ```shell
   python3 -m venv .venv
   source .venv/bin/activate
   ```

1. Install the requirements:

   ```shell
   pip install -r requirements.txt
   ```

1. Run the API via `uvicorn`

   ```shell
   uvicorn try_fastapi_chatgpt.application.api.fastapi:app
   ```

