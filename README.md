# Automated Phone System for Product Inquiry

## Overview
This project is an automated phone system designed to streamline and automate the process of handling customer inquiries about a specific product. It utilizes cutting-edge technologies to convert incoming voice calls into text, process the text using an AI language model (LLM), retrieve relevant information about the product from a vector database, generate a response, and convert it back into speech to play to the customer.

## Components
- **Voice-to-Text Conversion:** Converts incoming voice calls into text in real-time.
- **AI Language Model (LLM):** Processes the transcribed text to understand customer inquiries.
- **Vector Database:** Stores information about the specific product. Provides relevant data to the LLM for generating responses.
- **LangChain Framework:** Powers the LLM and facilitates its interaction with the vector database. Framework for developing applications powered by language models.
- **Response Generation and Speech Synthesis:** Generates a response based on the customer inquiry using LangChain. Converts the response back into speech using AI Eleven labs API.

## Workflow
1. When a customer calls, the voice is transcribed into text in real-time.
2. The transcribed text is fed into the AI language model (LLM) for processing.
3. The LLM retrieves relevant information about the product from the vector database.
4. Using the LangChain framework, the LLM generates a response based on the inquiry.
5. The response is converted back into speech using AI Eleven labs API.

## Benefits
- Enables efficient and accurate handling of customer inquiries.
- Reduces the need for human intervention, leading to cost savings and improved scalability.

## Setup and Installation
- Clone this repository to your local machine.
- Install the necessary dependencies.
- Configure the API keys and connection settings for LangChain and AI Eleven labs API.
- Deploy the system to your preferred hosting environment.
- Ensure proper integration with your phone system.

## Usage
- Ensure the system is running and properly configured.
- Customers can call the designated phone number to inquire about the product.
- The system will handle the inquiry automatically and provide a response in voice.

## Contributors
- **[Aymen noor]**
