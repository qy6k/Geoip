import requests

logo = r"""
________ _______ ________ ___ ________   
|\ ____\|\ ___ \ |\ __ \|\ \|\ __ \  
\ \ \___|\ \ __/|\ \ \|\ \ \ \ \ \ \|\ \
 \ \ \ __\ \ \_|/_\ \ \\\ \ \ \ \ ____\
  \ \ \|\ \ \ \_|\ \ \ \ \ \ \ \ \___|
   \ \_______\ \_______\ \_______\ \__\ \__\   
    \|_______|\|_______|\|_______|\|__|\|__| 
                                               
                                               
                                               
"""

def ip_lookup(ip_address=""):
    if not ip_address:
        print("Consultando IP do seu próprio dispositivo...")
    else:
        print(f"Consultando IP: {ip_address}")

    url = f"https://ipwho.is/{ip_address}" if ip_address else "https://ipwho.is/"

    try:
        response = requests.get(url)
        data = response.json()

        if not data.get("success", False):
            print("Erro na API:", data.get("message", "IP inválido"))
            return

        timezone = data.get("timezone") or {}
        connection = data.get("connection") or {}

        print("\n=== Informações de IP ===")
        print(f"IP: {data.get('ip')}")
        print(f"Continente: {data.get('continent')}")
        print(f"País: {data.get('country')} ({data.get('country_code')})")
        print(f"Região: {data.get('region')}")
        print(f"Cidade: {data.get('city')}")
        print(f"Latitude: {data.get('latitude')}")
        print(f"Longitude: {data.get('longitude')}")
        print(f"Fuso horário: {timezone.get('id')}")
        print(f"ISP: {connection.get('isp')}")
        print(f"Org: {connection.get('org')}")
        print(f"Tipo: {data.get('type')}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():
    print(logo)
    print("=== IP Lookup ===")
    while True:
        ip = input("Digite um IP para consultar (deixe vazio para seu IP, ou 'sair' para encerrar): ").strip()
        if ip.lower() == "sair":
            print("Encerrando o programa.")
            break
        ip_lookup(ip)
        print()

if __name__ == "__main__":
    main()