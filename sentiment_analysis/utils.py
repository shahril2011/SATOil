from bs4 import BeautifulSoup
import requests

def scrape_website(url):
    # Fetch the HTML content of the website
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the main content of the page
    main_content = extract_main_content(soup)

    return main_content

def extract_main_content(soup):
    # Find all div elements with class 'elementor-widget-container'
    main_content_divs = soup.find_all('div', class_='elementor-widget-container')

    # Check if the specified index is within the range of the found divs
    if len(main_content_divs) > 44:
        # Get the div at index 44
        target_div = main_content_divs[43]  # Index 44 corresponds to position 44-1 in Python

        # Extract text from p children of the target div
        p_children = target_div.find_all('p')
        main_text = "\n".join([p.get_text(separator='\n') for p in p_children])
        
        return main_text

    else:
        return "The specified index is out of range."