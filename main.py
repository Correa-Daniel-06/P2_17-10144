# Librerías a utilizar
import requests
import json
import csv
import time

# Clave de la API y URL base
API_KEY = "75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6"
API_URL = "https://api.meraki.com/api/v1"

# Función para obtener todas las organizaciones accesibles con la API Key
def get_organizations():
    headers = {
        "Content-Type": "application/json",
        "X-Cisco-Meraki-API-Key": API_KEY
    }
    response = requests.get(f"{API_URL}/organizations", headers=headers)
    return response.json()

# Función para obtener los dispositivos de una organización
def get_inventory(org_id):
    headers = {
        "Content-Type": "application/json",
        "X-Cisco-Meraki-API-Key": API_KEY
    }
    response = requests.get(f"{API_URL}/organizations/{org_id}/devices", headers=headers)
    devices = response.json()

    # Agrega una impresión para depurar
    print(f"Dispositivos obtenidos para la organización {org_id}:")
    print(json.dumps(devices, indent=4))

    # Filtrar dispositivos de tipo "wireless" o "appliance"
    filtered_devices = [
        {
            "name": device.get("name"),
            "model": device.get("model"),
            "mac": device.get("mac"),
            "serial": device.get("serial"),
            "public_ip": device.get("wan1Ip"),
            "lan_ip": device.get("lanIp"),
            "status": device.get("status"),
        }
        for device in devices
        if device.get("model") and ("wireless" in device.get("productType", "").lower() or "appliance" in device.get("productType", "").lower())
    ]

    # Imprimir dispositivos filtrados
    print(f"Dispositivos filtrados: {filtered_devices}")
    return filtered_devices

# Función para exportar dispositivos a un archivo CSV
def export_to_csv(devices, filename="inventario.csv"):
    if not devices:
        print("No hay dispositivos para exportar.")
        return

    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["name", "model", "mac", "serial", "public_ip", "lan_ip", "status"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(devices)
        print(f"Archivo {filename} generado con éxito.")

# Script principal
if __name__ == "__main__":
    while True:
        try:
            # Paso 1: Obtener organizaciones
            organizations = get_organizations()
            print("Organizaciones disponibles:")
            print(json.dumps(organizations, indent=4))

            # Paso 2: Generar inventario para cada organización
            all_devices = []
            for org in organizations:
                org_id = org["id"]
                org_name = org["name"]
                print(f"Obteniendo dispositivos para la organización: {org_name} (ID: {org_id})")
                devices = get_inventory(org_id)
                all_devices.extend(devices)  # Acumular dispositivos de todas las organizaciones

            # Paso 3: Exportar los dispositivos a un archivo CSV
            export_to_csv(all_devices)

            # Mensaje de éxito
            print("Inventario actualizado. Esperando 5 minutos para la próxima ejecución...")
        except Exception as e:
            print(f"Error: {e}")

        # Esperar 5 minutos antes de la próxima iteración
        time.sleep(300)
