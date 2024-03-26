import csv
import json

def convert_news_to_intents(csv_file, intents_file):
    intents = []

    # Đọc dữ liệu từ file tin tức CSV và tạo intents
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        news_count = 1  # Đếm số lượng tin tức
        for row in reader:
            intent = {
                "tag": f"news{news_count}",  # Sử dụng tag news1, news2, ...
                "patterns": [f"{row['title']}",f"{row['date']}"],
                "responses": [row["content"]],
                "context_set": ""
            }
            intents.append(intent)
            news_count += 1
    # Ghi các intents vào file intents.json
    with open(intents_file, 'w', encoding='utf-8') as file:
        json.dump(intents, file, ensure_ascii=False, indent=4)

convert_news_to_intents('vnexpress.csv', 'intents1.json')
