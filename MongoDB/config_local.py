from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError
import os

def connect_mongodb_local():
    """Kết nối MongoDB local với xử lý lỗi"""
    try:
        # Kết nối MongoDB local
        uri = "mongodb://localhost:27017/"
        
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        
        # Test kết nối
        client.admin.command('ping')
        print("✅ Kết nối MongoDB local thành công!")
        
        return client
        
    except ConnectionFailure as e:
        print(f"❌ Không thể kết nối MongoDB local: {e}")
        print("💡 Hãy đảm bảo MongoDB đang chạy trên localhost:27017")
        return None
        
    except Exception as e:
        print(f"❌ Lỗi không xác định: {e}")
        return None

def create_sample_data(client):
    """Tạo dữ liệu mẫu để test"""
    try:
        db = client['test_database']
        collection = db['test_collection']
        
        # Xóa dữ liệu cũ
        collection.delete_many({})
        
        # Thêm dữ liệu mẫu
        sample_data = [
            {"name": "Alice", "age": 25, "city": "New York"},
            {"name": "Bob", "age": 30, "city": "San Francisco"},
            {"name": "Charlie", "age": 35, "city": "Los Angeles"},
            {"name": "Diana", "age": 28, "city": "Chicago"},
            {"name": "Eve", "age": 32, "city": "Boston"}
        ]
        
        result = collection.insert_many(sample_data)
        print(f"✅ Đã tạo {len(result.inserted_ids)} documents mẫu")
        
        return collection
        
    except Exception as e:
        print(f"❌ Lỗi khi tạo dữ liệu mẫu: {e}")
        return None

def main():
    """Hàm chính để test kết nối MongoDB local"""
    client = connect_mongodb_local()
    
    if client is None:
        print("\n🔧 Hướng dẫn cài đặt MongoDB local:")
        print("1. Cài đặt MongoDB: brew install mongodb-community")
        print("2. Khởi động MongoDB: brew services start mongodb-community")
        print("3. Kiểm tra trạng thái: brew services list | grep mongodb")
        return
    
    try:
        # Tạo dữ liệu mẫu
        collection = create_sample_data(client)
        
        if collection is not None:
            # Lấy tất cả documents
            documents = collection.find()
            
            print(f"\n📊 Dữ liệu từ collection 'test_collection':")
            for i, doc in enumerate(documents, 1):
                print(f"\n--- Document {i} ---")
                print(f"Name: {doc.get('name', 'N/A')}")
                print(f"Age: {doc.get('age', 'N/A')}")
                print(f"City: {doc.get('city', 'N/A')}")
            
            # Thống kê
            total_docs = collection.count_documents({})
            print(f"\n📈 Tổng số documents: {total_docs}")
            
    except Exception as e:
        print(f"❌ Lỗi khi truy vấn dữ liệu: {e}")
        
    finally:
        client.close()
        print("\n🔌 Đã đóng kết nối MongoDB")

if __name__ == "__main__":
    main() 