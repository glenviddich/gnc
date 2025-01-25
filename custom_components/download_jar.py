import os
import requests
from homeassistant.const import DATA_DIR

def download_jar():
    """Lade die gn_server.jar-Datei herunter und speichere sie im Verzeichnis."""
    url = "https://gn.link/jar"
    jar_path = os.path.join(DATA_DIR, "gn_server", "gn_server.jar")
    
    if not os.path.exists(os.path.dirname(jar_path)):
        os.makedirs(os.path.dirname(jar_path))

    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(jar_path, "wb") as file:
                file.write(response.content)
            return True
        else:
            _LOGGER.error("Fehler beim Herunterladen der Datei: %s", response.status_code)
            return False
    except Exception as e:
        _LOGGER.error("Fehler beim Herunterladen der .jar-Datei: %s", str(e))
        return False
