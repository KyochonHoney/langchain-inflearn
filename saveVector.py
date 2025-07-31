from dotenv import load_dotenv
from docx import document_list
from langchain_upstage import UpstageEmbeddings
from langchain_chroma import Chroma
import os

load_dotenv()
api_key = os.getenv("UPSTAGE_API_KEY")
embeddings = UpstageEmbeddings(
    api_key=api_key,
    model="embedding-query"
)
 
database = Chroma.from_documents(
    documents=document_list,
    embedding=embeddings,
)


query = "연봉 5천만원인 직장인의 소득세는 얼마인가요?"
retrieved_docs = database.similarity_search(query)
print(retrieved_docs)
