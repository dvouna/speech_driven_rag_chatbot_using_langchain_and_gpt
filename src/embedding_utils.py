# import OpenAI Embeddings from langchain_openai
from langchain_openai import OpenAIEmbeddings

# Define embedding function 
embedding_function = OpenAIEmbeddings(api_key=openai_api_key, model='text-embedding-3-small') 