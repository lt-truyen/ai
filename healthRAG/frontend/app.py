import streamlit as st
import requests

st.title("🧠 Trợ lý AI Y tế – RAG")

question = st.text_input("Nhập câu hỏi y tế của bạn:")

if st.button("Gửi"):
    if question:
        response = requests.post("http://localhost:8000/query", json={"question": question})
        st.markdown("### ✅ Kết quả:")
        try:
            st.write(response.json()["answer"])
        except Exception as e:
            st.error(f"Lỗi phản hồi từ backend: {e}")
            st.text(response.text)