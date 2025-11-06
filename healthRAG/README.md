Tôi có thể giúp bạn tạo Prompt RAG, pipeline truy xuất, hoặc slide thuyết trình. Bạn muốn bắt đầu từ phần nào trước?

# 🧠 Medical RAG Assistant

Trợ lý AI chuyên ngành y tế sử dụng kỹ thuật Retrieval-Augmented Generation (RAG) để tra cứu triệu chứng, thuốc và kiến thức y khoa.

## 🚀 Tính năng
- Truy vấn tự nhiên bằng tiếng Việt
- Truy xuất tài liệu y khoa
- Phản hồi chính xác, có ngữ cảnh

## 🛠️ Cài đặt

### 1. Clone repo
```bash
git clone https://github.com/yourusername/rag-medical-assistant.git
cd rag-medical-assistant

#2. Cài backend &  backend
pip install -r requirements.txt
uvicorn main:app --reload
#3 run programe
streamlit run app.py