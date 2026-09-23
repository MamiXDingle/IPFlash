import socket
import requests
import time
def get_ip_locale():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_locale = s.getsockname()[0]
    s.close()
    return ip_locale

def get_ip_publique():
    try:
        response = requests.get('https://api.ipify.org')
        ip_publique = response.text.strip()
        return ip_publique
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de l'IP publique: {e}")
        return None

def main():
    ip_locale = get_ip_locale()
    ip_publique = get_ip_publique()

    if ip_publique:
        print(r"""
            ________  ________           __           
           /  _/ __ \/ ____/ /___ ______/ /_          
 ______    / // /_/ / /_  / / __ `/ ___/ __ \   ______
/_____/  _/ // ____/ __/ / / /_/ (__  ) / / /  /_____/
        /___/_/   /_/   /_/\__,_/____/_/ /_/          
                                                                    
              """)
        print('--------------- My IP is here! ---------------')
        print(f"--- Local IP  : {ip_locale}  ---")
        print(f"--- Public IP : {ip_publique} ---")
    else:
        print(f"Local IP : {ip_locale}")
        print("Impossible de récupérer l'adresse IP publique.")

if __name__ == "__main__":
    main()

    time.sleep(40)
