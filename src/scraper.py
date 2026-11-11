import requests
from bs4 import BeautifulSoup

URL = "https://www.cityu.edu.hk/ge_info/Search/"

def fetch_ge_courses():
    """Fetches and parses public Gateway Education course details."""
    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception(f"Failed to load page, status code: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    courses = []
    
    # Example parsing logic based on standard HTML tables
    # Adjust selectors according to the exact page markup structure
    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) >= 3:
            courses.append({
                "code": cols[0].text.strip(),
                "title": cols[1].text.strip(),
                "area": cols[2].text.strip()
            })
            
    return courses
