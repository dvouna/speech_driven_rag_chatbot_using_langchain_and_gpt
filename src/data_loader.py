# import necessary libraries
from langchain_community.document_loaders import PyPDFLoader

# Load Car Manual PDF
loader = PyPDFLoader(file_path="car_manual.pdf")
car_docs = loader.load() 