import os
from googlesearch import search

directory = ""  # Replace with the path to your files

# List of file names
file_names = [
    "8.txt", "35.txt", "48.txt", "49.txt", "62.txt", "69.txt", "92.txt", "93.txt", "94.txt", "95.txt",
    "96.txt", "109.txt", "112.txt", "114.txt", "115.txt", "131.txt", "134.txt", "135.txt", "136.txt",
    "156.txt", "180.txt", "181.txt", "182.txt", "183.txt", "214.txt", "229.txt", "288.txt", "289.txt",
    "290.txt", "291.txt", "292.txt", "345.txt", "350.txt", "351.txt", "352.txt", "353.txt", "354.txt",
    "420.txt", "421.txt", "422.txt", "423.txt", "428.txt", "464.txt", "469.txt", "470.txt", "471.txt",
    "472.txt", "473.txt", "474.txt", "475.txt", "507.txt", "533.txt", "571.txt", "572.txt", "573.txt",
    "574.txt", "575.txt", "576.txt", "577.txt", "618.txt", "627.txt", "628.txt", "629.txt", "630.txt",
    "631.txt", "632.txt", "633.txt", "634.txt", "635.txt", "678.txt", "702.txt", "703.txt", "728.txt",
    "747.txt", "748.txt", "749.txt", "750.txt", "751.txt", "752.txt", "753.txt", "754.txt", "768.txt",
    "787.txt", "788.txt", "789.txt", "790.txt", "791.txt", "792.txt", "793.txt", "794.txt", "831.txt",
    "837.txt", "838.txt", "839.txt", "840.txt", "841.txt", "842.txt", "843.txt", "844.txt", "845.txt",
    "846.txt", "853.txt", "855.txt", "860.txt", "861.txt", "886.txt", "888.txt", "919.txt", "981.txt",
    "982.txt", "983.txt", "984.txt", "985.txt", "986.txt", "987.txt", "988.txt", "989.txt", "990.txt",
    "991.txt", "992.txt", "993.txt", "994.txt", "995.txt", "1000.txt", "1001.txt", "1002.txt", "1003.txt",
    "1004.txt", "1048.txt", "1049.txt", "1050.txt", "1063.txt", "1065.txt", "1066.txt", "1067.txt",
    "1113.txt", "1114.txt", "1115.txt", "1116.txt", "1117.txt", "1118.txt", "1119.txt", "1120.txt",
    "1121.txt", "1122.txt", "1174.txt", "1183.txt", "1184.txt", "1190.txt", "1203.txt", "1206.txt",
    "1207.txt", "1208.txt", "1209.txt", "1210.txt", "1231.txt", "1232.txt", "1234.txt", "1282.txt",
    "1285.txt", "1286.txt", "1289.txt", "1346.txt", "1358.txt", "1385.txt", "1386.txt", "1387.txt",
    "1388.txt", "1389.txt", "1390.txt", "1392.txt", "1408.txt", "1409.txt", "1410.txt", "1411.txt",
    "1412.txt"
]

# Function to perform a Google search and get the author
def get_author_from_google_search(query):
    for j in search(query, num_results=1, stop=1, pause=2):
        if "hymnary.org/text" in j:
            response = requests.get(j)
            soup = BeautifulSoup(response.text, 'html.parser')
            author_tag = soup.find("meta", {"name": "author"})
            return author_tag["content"] if author_tag else None
    return None

# Loop through each file
for file_name in file_names:
    file_path = os.path.join(directory, file_name)
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().strip()

    # Construct search query and get author
    query = f"{content} site:hymnary.org/text"
    author = get_author_from_google_search(query)

    # Print the result
    print(f"File: {file_name}, Author: {author}")
