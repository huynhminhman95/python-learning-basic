import requests

url = "https://jsonplaceholder.typicode.com/users"

params = {'userId': 1}
try:
   response = requests.get(url, params=params, timeout=5)  # timeout sau 5 giây
   response.raise_for_status()
   #  data = response.json()

   # call get list users
   #  for user in data: 
   #      print(f"{user['id']}: {user['name']} - {user['email']}")

   # call get user by id
   if response.ok:
      posts = response.json()
      for post in posts:
         print(f"{post['id']} : {post['title']}")
except requests.exceptions.Timeout:
    print("⏱ Lỗi: Kết nối quá lâu, đã timeout!")
except requests.exceptions.ConnectionError:
    print("🔌 Lỗi: Không thể kết nối đến máy chủ!")
except requests.exceptions.HTTPError as e:
    print("📡 HTTP Error:", e)
except Exception as e:
    print("❌ Lỗi khác:", e)
