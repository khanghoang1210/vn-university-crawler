from bs4 import BeautifulSoup


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
    university["address"] = address
    university_info.append(university)
print(university_info)
print(len(university_info))