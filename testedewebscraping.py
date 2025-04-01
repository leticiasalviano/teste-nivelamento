import os
import requests
import shutil
from bs4 import BeautifulSoup

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", href=True)

    pdf_links = [link['href'] for link in links if "Anexo I" in link.get_text() or "Anexo II" in link.get_text()]

    os.makedirs("PDFs_ANS", exist_ok=True)

    
    for pdf_url in pdf_links:
        if pdf_url.startswith("/"):
            pdf_url = "https://www.gov.br" + pdf_url

        pdf_name = pdf_url.split("/")[-1]  
        pdf_path = os.path.join("PDFs_ANS", pdf_name)

        print(f"📥 Baixando {pdf_name}...")

        pdf_response = requests.get(pdf_url, headers=headers)
        if pdf_response.status_code == 200:
            with open(pdf_path, "wb") as pdf_file:
                pdf_file.write(pdf_response.content)
            print(f"✅ {pdf_name} salvo em PDFs_ANS/")
        else:
            print(f"❌ Erro ao baixar {pdf_name}")

    zip_filename = "PDFs_ANS.zip"
    shutil.make_archive("PDFs_ANS", 'zip', "PDFs_ANS")

    print(f"📦 Arquivos compactados em {zip_filename}!")

else:
    print(f"❌ Erro ao acessar a página. Código: {response.status_code}")