from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1500,
    chunk_overlap = 200,
)

loader = Docx2txtLoader("./law.docx")
document_list = loader.load_and_split(text_splitter=text_splitter)
