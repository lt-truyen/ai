import os
from dotenv import load_dotenv
from openai import AzureOpenAI

from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.embeddings import Embeddings

class DummyEmbedding(Embeddings):
    def embed_documents(self, texts):
        return vectors  # reuse the precomputed vectors

    def embed_query(self, text):
        return vectors[0]  # just return one vector for compatibility
load_dotenv()


os.environ["AZURE_OPENAI_EMBEDDING_API_KEY"] = "sk-bgnDyqRaqSjMYeQ2aGiqZg"
os.environ["AZURE_OPENAI_EMBEDDING_ENDPOINT"] = "https://aiportalapi.stu-platform.live/jpe"
os.environ["AZURE_OPENAI_EMBED_MODEL"] = "text-embedding-3-small"

os.environ["AZURE_OPENAI_LLM_API_KEY"] = "sk-OkmOJrHqYZb_V_bjOFnC2w"
os.environ["AZURE_OPENAI_LLM_ENDPOINT"] = "https://aiportalapi.stu-platform.live/jpe"
os.environ["AZURE_OPENAI_LLM_MODEL"] = "GPT-4o-mini"


# 1. Load tài liệu
loader = PyPDFLoader("../data/medical_guide.pdf")
docs = loader.load()

# 2. Khởi tạo Azure OpenAI clients
client_embed = AzureOpenAI(
    api_version="2024-07-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_EMBEDDING_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_EMBEDDING_API_KEY"),
)

llm_client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_LLM_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_LLM_API_KEY"],
    api_version="2024-07-01-preview"
)

# 3. Tạo embedding thủ công
def embed_texts(texts):
    response = client_embed.embeddings.create(
        model=os.environ["AZURE_OPENAI_EMBED_MODEL"],
        input=texts
    )
    return [r.embedding for r in response.data]

# 4. Tạo vectorstore
texts = [doc.page_content for doc in docs]
vectors = embed_texts(texts)
text_embeddings = list(zip(texts, vectors))
vectorstore = FAISS.from_embeddings(text_embeddings, DummyEmbedding())
retriever = vectorstore.as_retriever()

# 5. Prompt template
prompt_template = PromptTemplate.from_template(
    "Bạn là trợ lý y tế AI. Dựa trên ngữ cảnh sau, hãy trả lời câu hỏi:\n\n{context}\n\nCâu hỏi: {question}"
)

# 6. Hàm RAG thủ công
def run_rag(question: str) -> str:
    context_docs = retriever.invoke(question)
    context = "\n".join([doc.page_content for doc in context_docs])
    prompt = prompt_template.format(context=context, question=question)

    response = llm_client.chat.completions.create(
        model=os.environ["AZURE_OPENAI_LLM_MODEL"],
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content