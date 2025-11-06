import os

# Cấu trúc thư mục và các file cần tạo
project_structure = {
    "backend": ["main.py","rag_pipeline.py","requirements.txt"],
    "frontend": ["app.py","requirements.txt"],
    "data": ["medical_guide.pdf"],
    "": ["README.md"]  # "" đại diện cho thư mục gốc của dự án
}

def create_init_files():
    folders = [
    "retriever",
    "generator",
    "app"
    ]

    for folder in folders:
        init_path = os.path.join(folder, "__init__.py")
        with open(init_path, "w", encoding="utf-8") as f:
            pass

    print("✅ Đã thêm __init__.py vào các thư mục để đánh dấu là Python packages.")

def create_structure(base_path, structure):
    # Tạo thư mục gốc nếu chưa tồn tại
    if not os.path.exists(base_path):
        os.makedirs(base_path)
        print(f"📁 Đã tạo thư mục gốc: {base_path}")

    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder) if folder else base_path
        os.makedirs(folder_path, exist_ok=True)
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "w", encoding="utf-8") as f:
                pass  # Tạo file rỗng
            print(f"📄 Đã tạo file: {file_path}")
    
    print("\n✅ Đã tạo xong cấu trúc thư mục và file rỗng cho dự án RAG Q&A.")
# Gọi hàm để tạo cấu trúc trong thư mục rag_qa_project
create_structure(".", project_structure)
# Gọi hàm để tạo __init__.py trong các thư mục cần thiết
#create_init_files()
