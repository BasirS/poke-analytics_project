# web scraping attempt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://www.vgchartz.com/games/games.php"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

MAX_PAGES = 2
params = {
    "name": "Pokemon",
    "order": "Sales",
    "ownership": "Both",
    "direction": "DESC",
    "showtotalsales": "1",  
    "shownasales": "1",    
    "showpalsales": "1",   
    "showjapansales": "1", 
    "showothersales": "1",  
    "showpublisher": "0",
    "showdeveloper": "0",
    "showreleasedate": "0",
    "showlastupdate": "0",
    "showvgchartzscore": "0",
    "showcriticscore": "0",
    "showuserscore": "0",
    "showshipped": "0"
}

def scrape_page(page_number):
    params["page"] = page_number
    print(f"Scraping page {page_number}...")
    response = requests.get(BASE_URL, headers=HEADERS, params=params)
    
    if response.status_code != 200:
        print(f"Failed to fetch page {page_number}. Status code: {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("tr") 
    data = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 8:  
            data.append({
                "Position": cols[0].get_text(strip=True),
                "Game": cols[1].get_text(strip=True),
                "Console": cols[2].get_text(strip=True),
                "Total Sales (M)": cols[3].get_text(strip=True),
                "NA Sales (M)": cols[4].get_text(strip=True),
                "EU Sales (M)": cols[5].get_text(strip=True),
                "JP Sales (M)": cols[6].get_text(strip=True),
                "Other Sales (M)": cols[7].get_text(strip=True),
            })
    return data

def scrape_all_pages():
    all_data = []
    for page in range(1, MAX_PAGES + 1):
        page_data = scrape_page(page)
        if not page_data:
            break 
        all_data.extend(page_data)
        time.sleep(1) 
    return all_data


if __name__ == "__main__":
    results = scrape_all_pages()
    if results:
        df = pd.DataFrame(results)
        df.to_csv("pokemon_game_sales.csv", index=False)
        print("Sales data scraped and saved to 'pokemon_game_sales.csv'.")
    else:
        print("No data scraped.")


pokemon_sales_file = 'pokemon_game_sales.csv'
vgsales_file = 'vgsales.csv'

pokemon_sales_data = pd.read_csv(pokemon_sales_file)
vgsales_data = pd.read_csv(vgsales_file)

def clean_and_format_pokemon_data(pokemon_sales, vg_sales):
    rename_mapping = {
        "Position": "Rank",
        "Game": "Name",
        "Console": "Platform",
        "Total Sales (M)": "Global_Sales",
        "NA Sales (M)": "NA_Sales",
        "EU Sales (M)": "EU_Sales",
        "JP Sales (M)": "JP_Sales",
        "Other Sales (M)": "Other_Sales"
    }

    pokemon_sales = pokemon_sales.rename(columns=rename_mapping)

    common_columns = list(set(pokemon_sales.columns) & set(vg_sales.columns))

    pokemon_sales = pokemon_sales[common_columns].fillna(0)

    for column in ["Global_Sales", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]:
        if column in pokemon_sales.columns:
            pokemon_sales[column] = (
                pokemon_sales[column]
                .replace(r'[^\d.]', '', regex=True)
                .replace('', '0')
                .astype(float)
            )

    return pokemon_sales

cleaned_pokemon_data = clean_and_format_pokemon_data(pokemon_sales_data, vgsales_data)

output_path = 'pokemon_game_sales_cleaned_v2.csv'
cleaned_pokemon_data.to_csv(output_path, index=False)