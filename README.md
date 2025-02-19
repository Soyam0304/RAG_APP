📄 PDF Chatbot with Groq (RAG Application)
This project is a Retrieval-Augmented Generation (RAG) chatbot that allows users to upload a PDF document and interact with it by asking questions. It processes the PDF, extracts meaningful text, converts it into embeddings using Hugging Face, stores it in a FAISS vector database, and retrieves relevant context to generate responses using Groq’s LLM.

🚀 Use case example:
Imagine you have a 50-page research paper or legal document and need quick insights. Instead of manually reading it, this chatbot lets you ask specific questions and get AI-powered answers instantly!

📌 Features
✅ Upload a PDF – Extracts and processes text automatically.
✅ Ask questions – Interact with the document like a chatbot.
✅ Fast and efficient search – Uses FAISS for optimized vector search.
✅ Context-aware answers – Generates responses based on relevant sections.
✅ Simple and user-friendly UI – Built with Streamlit.
✅ Secure API integration – Uses Groq’s AI model for response generation.
🏗️ Project Workflow
1️⃣ PDF Upload & Processing
The user uploads a PDF file via the Streamlit UI.
The PyPDF2 library extracts text from the document.
The extracted text is split into smaller chunks for better processing.
2️⃣ Creating Embeddings & Storing in FAISS
Hugging Face embeddings are generated for each text chunk.
These embeddings are stored in a FAISS vector store for fast retrieval.
3️⃣ Answer Generation with Groq
When a user asks a question, the vector store searches for relevant chunks.
The retrieved text is passed to Groq’s LLM to generate an answer.
The answer is displayed in the chat interface.

🛠️ Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/your-username/pdf-chatbot.git
cd pdf-chatbot
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Set Up API Keys
Create a secrets.toml file in your Streamlit folder and add your Groq API key:
GROQ_API_KEY = "your_api_key_here"
4️⃣ Run the Chatbot
streamlit run main.py
📌 How It Works (With Examples)
Step 1: Upload a PDF
You upload a PDF file (e.g., "Data Science Research.pdf").
Step 2: Ask a Question
Example:
User: "What are the key findings of the research?"
Chatbot: "The research highlights that deep learning models outperform traditional machine learning methods in image recognition tasks, achieving a 95% accuracy rate..."
Step 3: Get AI-Powered Answers
The chatbot retrieves relevant sections from the PDF and generates an answer.
🔧 Technologies Used
Technology	Purpose
Streamlit	Interactive UI for chatbot
PyPDF2	Extracts text from PDF files
FAISS	Efficient vector search for retrieval
Hugging Face	Creates embeddings for text chunks
Groq API	AI model for generating responses
🎯 Future Enhancements
🔹 Support for multiple PDFs – Interact with multiple documents at once.
🔹 Better text chunking – Improve search accuracy.
🔹 Advanced UI – Add more features like document summaries.