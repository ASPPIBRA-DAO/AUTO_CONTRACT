import qrcode

# Fotos Aéreas
fotos_aereas = [
    "https://i.postimg.cc/rsJpjKWd/Aerofotografia-04.png",
    "https://i.postimg.cc/GmSH68fG/Aerofotografia-05.png",
    "https://i.postimg.cc/0yNztdV9/Aerofotografia-06.png",
    "https://i.postimg.cc/FsTRJkN8/Aerofotografia-07.png"
]

# Fotos de Casa
fotos_casa = [
    "https://i.postimg.cc/VLmrtcMr/Casa-01.png",
    "https://i.postimg.cc/nzqrsdhG/Casa-02.png",
    "https://i.postimg.cc/MH8ctCFL/Casa-03.png",
    "https://i.postimg.cc/CLTC6t8S/Casa-04.png"
]

# Plantas
plantas = [
    "https://i.postimg.cc/MZsBCmG3/Distrito.png",
    "https://i.postimg.cc/8CDsJ75r/Pl-baixa-01.png",
    "https://i.postimg.cc/3x2dxXKT/Pl-baixa-02.png",
    "https://i.postimg.cc/htRt6XV3/Pl-cadastral.png",
    "https://i.postimg.cc/1RTt0CXS/Pl-situa-o.png"
]

# Certidões
certidoes = [
    "https://i.postimg.cc/4324mDGc/Art.png",
    "https://i.postimg.cc/GhvpqgP0/Ata-notarial.png",
    "https://i.postimg.cc/44DdvR9b/Declarat-ria.png",
    "https://i.postimg.cc/2yBsjJjC/nus-reais.png"
]

# Função para gerar e salvar QR codes
def gerar_qrcode(lista, categoria):
    for item in lista:
        meu_qrcode = qrcode.make(item)
        meu_qrcode.save(f"qrcode_{categoria}_{item.split('/')[-1]}.png")

# Gerar QR codes para cada categoria
gerar_qrcode(fotos_aereas, "Fotos_Aereas")
gerar_qrcode(fotos_casa, "Fotos_Casa")
gerar_qrcode(plantas, "Plantas")
gerar_qrcode(certidoes, "Certidoes")
