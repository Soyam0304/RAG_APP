from groq import Groq

# Initialize Groq client
client = Groq(api_key="YOUR_GROQ_API_KEY")  # Replace with your actual API key

def generate_answer(question, vector_store):
    """Generates an answer for the given question using the FAISS vector store and Groq API."""
    
    # Search for relevant chunks
    docs = vector_store.similarity_search(question, k=5)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    # Create prompt
    prompt = f"""
    You are a helpful assistant that answers questions based on the provided context.
    Context: {context}
    
    Question: {question}
    
    Provide a detailed, comprehensive answer using the context. If the answer isn't in the context,
    state that clearly. Ensure your answer is thorough and well-explained.
    Answer:
    """
    
    # Generate response using Groq
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="mixtral-8x7b-32768",
        temperature=0.3,
        max_tokens=2048
    )
    
    return response.choices[0].message.content
