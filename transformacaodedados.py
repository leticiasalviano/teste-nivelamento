import os
import requests
import pdfplumber
import pandas as pd
import shutil  


seu_nome = "Leticia"  


pdf_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

os.makedirs("PDFs_ANS", exist_ok=True)
pdf_path = os.path.join("PDFs_ANS", "Anexo-I.pdf")

if not os.path.exists(pdf_path):
    print(f"📥 Baixando {pdf_url}...")
    response = requests.get(pdf_url)
    if response.status_code == 200:
        with open(pdf_path, "wb") as pdf_file:
            pdf_file.write(response.content)
        print(f"✅ PDF salvo em {pdf_path}")
    else:
        print(f"❌ Erro ao baixar o PDF. Código: {response.status_code}")
        exit()

data_frames = []  
print("🔍 Extraindo tabelas do PDF...")

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages, start=1):
        tables = page.extract_tables()
        if tables:
            for table in tables:
                df = pd.DataFrame(table) 
                data_frames.append(df)

if data_frames:
   
    final_df = pd.concat(data_frames, ignore_index=True)

    if all(str(col).isdigit() for col in final_df.columns):
        final_df.columns = [
            "PROCEDIMENTO", "RN", "VIGÊNCIA", "OD", "AMB", "HCO", "HSO", "REF", 
            "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"
        ]

   
    csv_filename = "Tabela_Rol_Procedimentos.csv"
    csv_path = os.path.join("PDFs_ANS", csv_filename)
    final_df.to_csv(csv_path, index=False, encoding="utf-8-sig")

    print(f"📄 Tabela estruturada salva em {csv_path}!")

    legenda = {
        "OD": "Procedimentos Odontológicos",
        "AMB": "Procedimentos Ambulatoriais"
    }
    final_df.rename(columns=legenda, inplace=True)

    final_df.to_csv(csv_path, index=False, encoding="utf-8-sig")

    print(f"✅ Colunas renomeadas com sucesso!")

    zip_filename = f"Teste_{seu_nome}.zip"
    shutil.make_archive(f"Teste_{seu_nome}", 'zip', "PDFs_ANS")

    print(f"📦 Arquivo compactado como {zip_filename}!")

else:
    print("❌ Nenhuma tabela encontrada no PDF.")
