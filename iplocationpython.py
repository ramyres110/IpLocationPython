import requests

# URLs da APIs
api_ip = "https://api.ipify.org?format=json"

api_localizacao = "https://ipinfo.io/{}/geo"

# Requisição
print("Buscando IP...")
req = requests.get(api_ip)
if req.status_code == 200:
    ip_objeto = req.json()
    ip = ip_objeto["ip"]

    url_localizacao = api_localizacao.format(ip)
    print("Buscando localização...")
    req = requests.get(url_localizacao)
    if req.status_code == 200:
        localizacao = req.json()
        print("Resposta:")
        print("\tCidade: {}  ".format( localizacao["city"]))
        print("\tEstado: {} ".format( localizacao["region"]))
        print("\tPais: {} ".format( localizacao["country"]))
        print("\tLat e Lon: {} ".format( localizacao["loc"]))
        print("\tCEP: {} ".format( localizacao["postal"]))
        print("\tTimezone: {} ".format( localizacao["timezone"]))
else:
    print("Error - Status code {}".format(req.status_code))
