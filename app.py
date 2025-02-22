import requests
from bs4 import BeautifulSoup

job_ocupation = str(input("Digite o nome da profissão: "))
job_location = str(input("Digite o país: "))

def findJobs(keyword=job_ocupation, local=job_location, pagination=10):
    url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}&location={local}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Erro ao acessar o site.")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    array_jobs = []
    
    for job_card in soup.find_all("div", class_="job-search-card")[:pagination]:
        title = job_card.find("h3", class_="base-search-card__title").text.strip() if job_card.find("h3", class_="base-search-card__title") else "Sem título"
        business = job_card.find("h4", class_="base-search-card__subtitle").text.strip() if job_card.find("h4", class_="base-search-card__subtitle") else "Empresa não informada"
        location = job_card.find("span", class_="job-search-card__location").text.strip() if job_card.find("span", class_="job-search-card__location") else "Localização não informada"
        link = job_card.find("a")["href"] if job_card.find("a") else "Sem link"
        
        array_jobs.append({
            "Título": title,
            "Empresa": business,
            "Localização": location,
            "Link": link
        })
    
    return array_jobs

if __name__ == "__main__":
    list_jobs = findJobs()
    for i, job in enumerate(list_jobs, 1):
        print(f"{i}. {job['Título']} - {job['Empresa']} ({job['Localização']})")
        print(f"Link: {job['Link']}\n")