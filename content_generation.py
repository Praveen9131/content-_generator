import os
from flask import Flask, request, jsonify
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

KEY = os.getenv("OPENAI_API_KEY")

def generate_content(topic, desired_word_count):
    llm = ChatOpenAI(openai_api_key=KEY, model_name="gpt-4", temperature=1.0)
    
    # Estimate token count needed for desired word count
    estimated_tokens = int(desired_word_count * 1.3)  # Rough estimation
    
    content = ""
    current_word_count = 0
    
    while current_word_count < desired_word_count:
        remaining_words = desired_word_count - current_word_count
        extra_tokens = int(remaining_words * 1.3)  # Continue estimating needed tokens

        predefined_text = f"Based on the fundamentals of {topic}, create content that encompasses the core concepts and challenges students' understanding. Provide a complete, concise explanation and conclusion."
        template = f"Text: {predefined_text} You are an expert content generator. Continue the text to elaborate on {topic}, aiming for an additional {remaining_words} words. Ensure all sentences are complete and wrap up the discussion comprehensively within the total word count of {desired_word_count}."

        
        prompt_template = PromptTemplate(input_variables=["topic"], template=template)
        llm_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="content")
        
        response = llm_chain({"topic": topic})
        generated_text = response.get("content", "")
        
        # Append new content and update word count
        content += " " + generated_text
        current_word_count = len(content.split())

    # Return the content trimmed to the exact desired word count
    final_content = ' '.join(content.split()[:desired_word_count])
    return final_content

@app.route('/generate', methods=['GET'])
def generate_api():
    topic = request.args.get('topic')
    words = request.args.get('words', type=int)
    content = generate_content(topic, words)
    return jsonify({"content": content})

if __name__ == '__main__':
    app.run(debug=True, port=5050)
