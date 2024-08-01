# Personal Movie Assistant

A chatbot application designed to assist users in exploring and discovering movies. This project uses Python with a PyQt5-based graphical user interface and advanced language modeling via the Ollama LLM (Llama 3.1) for generating personalized responses.

## Features

- **Movie Recommendations**: Offers personalized movie recommendations based on user preferences, including genre, favorite actors, and desired year range.
- **Detailed Movie Information**: Fetches and displays detailed information about movies, including titles, release dates, overviews, ratings, and more, using The Movie Database (TMDb) API.
- **Interactive GUI**: A user-friendly interface built with PyQt5, featuring a chat-based interaction system.
- **Conversation History**: Maintains a history of user interactions to provide context-aware responses.
- **Advanced Language Model**: Utilizes the Ollama LLM (Llama 3.1) to generate detailed and contextually accurate responses to user queries.

## Prerequisites

- **Python**: Ensure Python is installed on your machine.
- **PyQt5**: For GUI components.
- **Ollama**: Install the Ollama platform on your machine.
- **Llama 3.1**: Download and configure the Llama 3.1 model.
- **TMDb API Key**: Obtain a key from [TMDb](https://www.themoviedb.org/) and set it in your environment variables as `TMDB_API_KEY`.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/your-username/your-repository-name.git](https://github.com/asultanli/Personal-Movie-Assistant.git)
   cd Personal-Movie-Assistant
   ```

2. **Install Python Packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup TMDb API Key**:
   - Obtain an API key from [TMDb](https://www.themoviedb.org/).
   - Set it in your environment variables as `TMDB_API_KEY`.

4. **Install Ollama and Llama 3.1**:
   - Follow the installation instructions for Ollama and download the Llama 3.1 model from the official sources.
   - Ensure they are correctly configured and accessible on your system.

## Running the Application

1. **Start the Chatbot**:
   - Run the application using the command:
     ```bash
     python3 main.py
     ```

2. **Interacting with the Chatbot**:
   - Use the GUI to enter your queries about movies or ask for recommendations.
   - The chatbot will provide responses based on the integrated API data and user preferences, leveraging the advanced capabilities of the Ollama LLM.

