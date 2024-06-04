
# Content Generator

This project is a FastAPI-based web application designed to generate articles using OpenAI's GPT-3.5-turbo-16k model. The application can process multiple sections, each with specified titles and word counts, ensuring the generated text is coherent, well-organized, and meets the word count requirements. The application also supports saving conversation history and prefixing prompts with additional context.

## Features

- Generate text sections with specified titles and word counts.
- Ensure generated text consists of complete sentences.
- Adjust the word count of generated text to fit within specified ranges.
- Save conversation history for consistent context across multiple requests.
- Add prefixes to prompts to provide additional context for the generated text.
- Round-robin usage of multiple OpenAI API keys to manage rate limits.

## Prerequisites

- Python 3.8 or higher
- An OpenAI API key (or multiple keys)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Praveen9131/content-_generator.git
   cd content-_generator
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:** 

   Create a `.env` file in the root directory of the project and add your OpenAI API keys. Use the following format:

   ```env
   OPENAI_API_KEY_1=your_first_api_key
   OPENAI_API_KEY_2=your_second_api_key
   ```

## Usage

1. **Start the FastAPI application:**

   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

2. **Send a POST request to the `/generate-article` endpoint:**

   The request body should be a JSON object with the following structure:

   ```json
   {
     "sections": [
       {
         "title": "Introduction to AI",
         "word_count": "100 to 200"
       },
       {
         "title": "Applications of AI",
         "word_count": "150"
       }
     ],
     "prefixes": [
       "AI is a rapidly growing field.",
       "It has many applications in different industries."
     ],
     "save_conversation_history": true
   }
   ```

   - `sections`: A list of sections to generate, each with a `title` and `word_count`. The `word_count` can be a specific number or a range (e.g., "100 to 200").
   - `prefixes`: (Optional) A list of prefixes to add context to the prompts.
   - `save_conversation_history`: (Optional) A boolean flag to save the conversation history between requests.

3. **Example request using `curl`:**

   ```sh
   curl -X POST "http://localhost:8000/generate-article" -H "Content-Type: application/json" -d '{
     "sections": [
       {
         "title": "Introduction to AI",
         "word_count": "100 to 200"
       },
       {
         "title": "Applications of AI",
         "word_count": "150"
       }
     ],
     "prefixes": [
       "AI is a rapidly growing field.",
       "It has many applications in different industries."
     ],
     "save_conversation_history": true
   }'
   ```

## API Endpoints

### POST `/generate-article`

Generates articles based on the provided sections, prefixes, and options to save conversation history.

- **Request Body:**

  ```json
  {
    "sections": [
      {
        "title": "Section Title",
        "word_count": "Word Count Range or Specific Count"
      }
    ],
    "prefixes": ["Optional Prefixes"],
    "save_conversation_history": false
  }
  ```

- **Response:**

  ```json
  {
    "result": [
      {
        "title": "Section Title",
        "content": "Generated content...",
        "word_count": 150
      }
    ]
  }
  ```

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- OpenAI for providing the GPT-3.5-turbo-16k model.
- FastAPI for the web framework.

## Contact

For any questions or suggestions, please open an issue on GitHub.
