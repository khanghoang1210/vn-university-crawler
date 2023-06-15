from bs4 import BeautifulSoup
import json

# Open the text file in read mode
file_path = "./html.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    # Read the entire content of the file into a string
    html = file.read()

    
soup = BeautifulSoup(html,'html.parser')
table = soup.find('tbody')
rows = table.find_all('tr')
university_info = []
for row in rows:
    university = {}
    columns = row.find_all('td')
    university_name = columns[1].text.strip()
    address = columns[2].text.strip()

    university["name"] = university_name
    keyword = "Điện thoại" or "Tel"
    start_index = address.find(keyword)
    if start_index != -1:
        university["address"] = address.replace(" –", ",")[9:start_index]
    else:
        university["address"] = address.replace(" –", ",")[9:]
    university_info.append(university)
print(university_info)
print(len(university_info))


# Lưu danh sách vào tệp JSON
with open('university.json', 'w',encoding='utf-8') as file:
    json.dump(university_info, file, ensure_ascii=False, indent=4)