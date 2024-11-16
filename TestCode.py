

"""
from colorama import Fore, Style
import nmap

print(Fore.CYAN + Style.BRIGHT + "Scanning Configuration..." + Style.RESET_ALL)

nm = nmap.PortScanner()  # Initialize PortScanner object

while True:
    print("")
    ip_range = input(
        Fore.CYAN +
        "Entrez la plage d'adresses IP à scanner (ex : 192.168.1.1/24)\n- 'r' Pour revenir au menu : "
    )
    print("")
    print("-------------------------------------------------------------------------------" + Style.RESET_ALL)
    print("")

    if ip_range.lower() == 'r':
        break

    try:
        nm.scan(hosts=ip_range, arguments='-sV -p 1-1024')  # Nmap scan
        print(Fore.YELLOW + Style.BRIGHT + "Analyse terminée...Résultats du scan:" + Style.RESET_ALL)
        print("")
        
        for idx, host in enumerate(nm.all_hosts(), start=1):  # Add indexing for hosts
            print(f"Host {idx}: {host}")
            for proto in nm[host].all_protocols():
                print(f"  Protocol: {proto}")
                lport = nm[host][proto].keys()
                for port in lport:
                    print(f"    Port: {port} ({nm[host][proto][port]['state']})")
                    print(f"    Service: {nm[host][proto][port]['name']}")
                    print(f"    Version: {nm[host][proto][port]['version']}")
            print("")
        
        while True:  # Allow saving results
            fichier_nmap = input(
                "Pour sauvegarder le scan dans un fichier conf, entrez le numéro de host à sauvegarder ou 'r' pour revenir au menu : "
            )

            if fichier_nmap.lower() == 'r':
                break

            try:
                num_host = int(fichier_nmap)
                if 1 <= num_host <= len(nm.all_hosts()):
                    selected_host = nm.all_hosts()[num_host - 1]
                    # Logic for saving `selected_host` results to a file can go here
                    print(f"Host {num_host} selected: {selected_host}")
                else:
                    print("Numéro de host invalide. Essayez encore.")
            except ValueError:
                print("Entrée non valide. Entrez un numéro ou 'r' pour revenir au menu.")

    except Exception as e:
        print(Fore.RED + f"Erreur: {e}" + Style.RESET_ALL)


                    nom_ser_nmap = input(Fore.CYAN + "Entrer le nom du Serveur: ")

                    nom_fichier_conf_nmap = input(Fore.CYAN + "Entrer le nom du fichier (suggestion: nom du serveur): ")
                    
                    nom_fichier_conf_choisi_nmap = nom_fichier_conf_choisi_nmap + ".json" 
                    
                    server_config_nmap_nmap = {"Host": host , "Ip": ip_ser , "Systeme":sys_exp, "Services UP":services_up}  

                    with open(nom_fichier_conf_choisi_nmap, 'w') as f: #crée le fichier.json et le met en mode write.
                        json.dump(server_config_nmap_nmap, f, indent=4) #dump: écris ajoute l'information dans le fichier, indent donne le forma pour qu'il soit lisible en json
                            

"""                          


import json
from colorama import Fore, Style
import nmap

nm = nmap.PortScanner() # Démarre l'objet PortScanner


scan_results = {} 
    
    


print("")
ip_range = input(Fore.CYAN + "Entrez la plage d'adresses IP à scanner (ex : 192.168.1.1/24)\n- 'r' Pour revenir au menu : ") # Définie le  la porté de le scan IP  (e.g. 192.168.1.0/24)
print("")
print("-------------------------------------------------------------------------------" + Style.RESET_ALL)
print("")

print(Fore.YELLOW + Style.BRIGHT + "Scanning..." + Style.RESET_ALL)

nm.scan(hosts=ip_range, arguments='-sV -p 1-1024') # -sV : scan et identifie la version de chaque service. -p scan les ports dans l'IP range.


# Process the results
print(Fore.YELLOW + Style.BRIGHT + "Analyse terminée...Résultats du scan:" + Style.RESET_ALL)

for index, host in enumerate(nm.all_hosts(), start=1):
    print(f"{index}. Host : {host}")
    host_info = {"protocols": {}}
    for proto in nm[host].all_protocols():
        print(f"    Protocol: {proto}")
        ports = []
        for port in nm[host][proto].keys():
            port_info = {
                "port": port,
                "state": nm[host][proto][port]['state'],
                "service": nm[host][proto][port]['name'],
                "version": nm[host][proto][port]['version']
            }
            ports.append(port_info)
            print(f"    Port: {port} ({port_info['state']})")
            print(f"    Service: {port_info['service']}")
            print(f"    Version: {port_info['version']}")
            print("")
        host_info["protocols"][proto] = ports  # Store protocol-level details

    # Save information for the host
    scan_results[host] = host_info

# Display stored data for debugging
print(Fore.CYAN + Style.BRIGHT + "Stored Scan Results:" + Style.RESET_ALL)
print(json.dumps(scan_results, indent=4))

# Allow saving a specific host to a JSON file
while True:
    host_index = input(
        "Entrez le numéro de l'hôte à sauvegarder dans un fichier JSON ou 'r' pour revenir au menu : "
    )
    if host_index.lower() == 'r':
        break
    try:
        host_index = int(host_index) - 1
        if 0 <= host_index < len(nm.all_hosts()):
            selected_host = nm.all_hosts()[host_index]
            with open(f"{selected_host}.json", "w") as json_file:
                json.dump({selected_host: scan_results[selected_host]}, json_file, indent=4)
            print(Fore.GREEN + f"Les résultats pour {selected_host} ont été sauvegardés dans {selected_host}.json" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Numéro d'hôte invalide. Essayez encore." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Entrée non valide. Entrez un numéro ou 'r' pour revenir au menu." + Style.RESET_ALL)
