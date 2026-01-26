
import re

input_path = r'c:\Users\Данис\Desktop\antigravity-task-1\extracted_text.txt'
output_path = r'c:\Users\Данис\Desktop\antigravity-task-1\analysis_results.txt'

keywords = {
    "Strategy/Digital/Product": [r"Стратеги", r"Цифров\w+\s+трансформаци", r"Продукт"],
    "IT/Tech/Eng": [r"\bИТ\b", r"\bIT\b", r"Технологи", r"Программное обеспечение", r"Разработка", r"Инженер", r"5G", r"LTE"],
    "Funding/CAPEX": [r"Бюджет", r"CAPEX", r"Капитальные затраты", r"Капвложения", r"Нематериальные активы", r"Инвестици"],
    "Metrics": [r"Абонент", r"Отток", r"Выручка", r"ARPU", r"MOU", r"Доход"],
    "Agile/Teams/Customer": [r"Agile", r"Аджайл", r"Команд", r"Клиентоцентричность", r"Клиент"]
}

try:
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    results = ""

    for category, patterns in keywords.items():
        results += f"\n=== {category} ===\n"
        found_in_category = False
        for pattern in patterns:
            matches = list(re.finditer(pattern, content, re.IGNORECASE))
            if matches:
                # Limit to first 5 matches per keyword to avoid flooding if common word
                for match in matches[:5]: 
                    start = max(0, match.start() - 200)
                    end = min(len(content), match.end() + 200)
                    snippet = content[start:end].replace("\n", " ")
                    results += f"Match '{pattern}': ...{snippet}...\n---\n"
                    found_in_category = True
        
        if not found_in_category:
            results += "No matches found.\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(results)
    
    print(f"Analysis complete. saved to {output_path}")

except Exception as e:
    print(f"Error analyzing text: {e}")
