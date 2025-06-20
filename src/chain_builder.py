# Import necessary modules
from langchain_core.runnables import RunnablePassthrough

# Define RAG chain
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()} 
    | prompt 
    | llm 
)