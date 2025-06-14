# UNG DUNG CHUYEN DOI NGON NGU
# Bien doi cac chu cai co dau thang khong dau
# á à ả ã ạ ă ắ ằ ẵ ặ â ấ ầ ẩ ẫ ậ ---> a
# Vi du:
# Huỳnh Minh Mẫn -> Huynh Minh Man

text_vi = "áàảãạăắằẵặâấầẩẫậ"

def translate(text):
     translation = ""
     for char in text:
         if char.lower() in text_vi:
             if char.isupper():
                 translation = translation + "A"
             else:
                translation = translation + "a"
         else:
             translation = translation + char

         # text = "Mẫn"
         # char = "M" ---> translation = "" + "M" = "M"
         # char = "ẫ" ---> translation = "M" + "a" = "Ma"
         # char = "n" ---> translation = "Ma" + "n" = "Man"
     return translation

name = input("Nhap vao ten ma ban muon bien dich: ")
print(translate(name))