# FastAPI ChatGPT Sample Project

This repository contains a sample project that demonstrates how to integrate
[FastAPI](https://fastapi.tiangolo.com/) with ChatGPT, a powerful language model developed by OpenAI.
With this project, you can create a simple web application that allows users to
interact with ChatGPT through a RESTful API. The API's sole capability is to
request travel recommendations from ChatGPT given a country and a season.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.8+
- An OpenAI API key (Sign up at [OpenAI](https://beta.openai.com/signup/) and follow their API key setup instructions)
- [Docker](https://www.docker.com)
## Run Using Docker

1. Build the image:
   
   ```shell
   docker build -t try-fastapi-chatgpt:latest .
   ```

2. Run a container based from the image:

   ```shell
   docker run --rm -p 3000:3000 -e "OPENAI_API_KEY=sk-YOURSECRETKEY" try-fastapi-chatgpt:latest
   ```

## Getting Started for Development

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/pilosoposerio/try-fastapi-chatgpt.git
   cd try-fastapi-chatgpt
   ```

2. Create a Python virtual environment:

   ```shell
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the requirements:

   ```shell
   pip install -r requirements.txt
   ```

4. Run the API via `uvicorn`

   ```shell
   uvicorn try_fastapi_chatgpt.application.api.fastapi:app --reload --port 3000
   ```