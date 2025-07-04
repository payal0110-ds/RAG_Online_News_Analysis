# CODE 1: DataIngestion

Loads a PDF file and split its text into overlapping chunks using the `langchain_community` and `langchain_text_splitter` rexpectively.

> Loads the PDF file from the repository. 
> Splits the PDF files into "Chunks" using `__RecursiveCharacterTextSplitter__` where the chunk_size is `500` & chunk_overlap size is `50`.
> Chunks are stores as list of "Document object" which can be retrieved manually by simple indexing technique.


# CODE 2: Embedding

Converts the PDF chunks into vector embeddings and save them in FAISS vector DB locally.

> Calls `PDF_Load` function to split the PDF into text chunks.
> Splits the PDF docs into chunks which is done by the module __PDF_Load__.
> Loads the embedding model __Gemma 2b:2__, then converts the chunks into vector embeddings.
> Finally stores the vector embeddings in a __FAISS index__ locally.

# CODE 3: Retriever

Sets a pipeline for a basic `RAG application` and deploy a minimal `Streamlit web app` where it allows the users to ask questions and the system fetches relevant context from a saved `FAISS Vector DB`, then use and `LLM(Gemma 2B from Ollama)` to answer the questions. 

> Loads the saved Vector DB of documents.
> Converts the user queries into vectors using the same embedding model (Gemma2b:2 from Ollama). 
> Creates the prompts and initializes the LLM model, then wraps/links the prompts and LLM model.
> Using the saved Vector DB as a retriever to retrieve the relavant documents, which will be displayed in a Streamlit based web application where the users ask the questions.

__NOTE:__ __NOTE:__ This code should be run in command prompt with command `'streamlit run path/filename'` and to terminate the streamlit server, press `control+C (^+C)`.
