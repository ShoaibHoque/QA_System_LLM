# **Question Answering System for Bangla and English**

This project demonstrates a multilingual question-answering system using **LangChain**, **ChatGroq**, and **FAISS** to handle both general and personalized questions. The system integrates a retrieval-augmented generation (RAG) approach with fallback capabilities to provide answers based on indexed personal data or general knowledge.

## Features
- **Dynamic QA:** Handles Bangla and English queries.
- **RAG-Based Retrieval:** Fetches relevant information from indexed personal data (e.g., a resume).
- **General Knowledge Support:** Falls back to the LLM (LLaMA 3.1) when no relevant documents are found.
- **Streamlit Integration:** A user-friendly interface for interactive Q&A.

## Installation
### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/qa-system.git
cd qa-system
```

### Step 2: Install Dependencies
Ensure you have Python 3.9+ installed. Install the required Python libraries:
```bash
pip install -r requirements.txt
```
### Step 3: Prepare Your Personal Data
Place your resume or personal documents in the root directory as a text file named `resume.txt`. For example:

```text
resume.txt
```
If you have additional personal data, replace `resume.txt` with your own file and modify the `TextLoader` file path in the code.

### Step 4: Set Up Environment Variables
Create a `.env` file in the project directory and add your **Groq API Key**:
```env
GROQ_API=your_groq_api_key
```
## Usage
### Run the Streamlit App
Start the Streamlit application:
```bash
streamlit run app.py
```
#### Interact with the App
- Enter your questions in the text input box.
- Click the "Get Answer" button to generate a response.
- The system provides answers based on:
  - **Indexed personal data:** Answers from your uploaded documents.
  - **General knowledge fallback:** Answers from the LLaMA model for unrelated queries.

## Project Structure
```plaintext
qa-system/
├── app.py              # Main application script
├── resume.txt          # Example resume file (replace with your own)
├── requirements.txt    # Required Python libraries
├── .env                # Environment variables (for Groq API key)
└── README.md           # Project documentation
```
## How It Works
1. **Personal Data Retrieval:**

  - Loads personal data from `resume.txt`.
  - Creates vector embeddings using `sentence-transformers/all-mpnet-base-v2`.
  - Stores embeddings in a FAISS vector database.
2. **LLM Integration:**

  - Leverages the Groq API to interact with the LLaMA 3.1 model.
  - Handles fallback to LLM when no personal data is relevant.
3. **Streamlit Frontend:**

  - Provides an interactive UI to input questions and display results.
4. **Custom QA Logic:**

  - First attempts to fetch relevant context using FAISS retriever.
  - Uses the retriever’s results to form a context-aware prompt.
  - Falls back to general knowledge from the LLM if no relevant context is found.

## Customization
1. **Change Model or Data:**

- Modify the `HuggingFaceEmbeddings` model or upload a different dataset for indexing.
2. **Extend to Multiple Documents:**

- Update `TextLoader` to load multiple files or use other loaders from LangChain.
3. **Add More Languages:**

- Replace `sentence-transformers/all-mpnet-base-v2` with multilingual models.

## Dependencies
Below are the main dependencies for the project:

- **LangChain** for chain creation and document handling.
- **FAISS** for vector similarity search.
- **Hugging Face** for embedding models.
- **ChatGroq** for LLM integration.
- **Streamlit** for the user interface.
- 
Install these libraries using `requirements.txt`:
```plaintext
langchain
langchain_community
langchain_huggingface
langchain_groq
streamlit
```
## Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`feature/my-feature`).
3. Commit your changes and push.
4. Submit a pull request.

## Contact
For any questions or feedback, please contact:

- **Name:** Shoaib Hoque
- **Email:** shoaibhoque@gmail.com
- **LinkedIn:** [Shoaib Hoque](https://www.linkedin.com/in/shoaib-hoque-2bb20314b/)
- **GitHub:** [ShoaibHoque](https://github.com/ShoaibHoque)

