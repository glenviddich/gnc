import subprocess
import logging

_LOGGER = logging.getLogger(__name__)

# Starten einer Instanz des gn_server.jar auf dem angegebenen Port
def start_gn_server_instance(port):
    """Starte eine Instanz des gn_server.jar auf dem angegebenen Port."""
    try:
        subprocess.Popen(
            ["java", "-jar", "/config/custom_components/gnc/gn_server.jar", f"-p", f"{port}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        _LOGGER.info(f"Starte gn_server.jar auf Port {port}")
    except Exception as e:
        _LOGGER.error(f"Fehler beim Starten des gn_server auf Port {port}: {e}")

# Starten mehrerer Instanzen des gn_server.jar auf verschiedenen Ports
def start_multiple_instances(ports):
    """Starte mehrere Instanzen des gn_server.jar auf verschiedenen Ports."""
    for i, port in enumerate(ports):
        if i == 0:
            start_gn_server_instance(port)

# Stoppen aller laufenden gn_server Instanzen
def stop_gn_server_instance():
    """Stoppe alle laufenden gn_server Instanzen."""
    try:
        for pid in os.popen("pgrep -f 'gn_server.jar'").read().splitlines():
            os.kill(int(pid), signal.SIGTERM)
        _LOGGER.info("Alle gn_server Instanzen gestoppt.")
    except Exception as e:
        _LOGGER.error(f"Fehler beim Stoppen des gn_server: {e}")

# Einrichten der Dienste in Home Assistant
async def async_setup(hass, config):
    """Setze die Integration auf."""
    hass.services.async_register(
        "gnc", "start_server", start_multiple_instances
    )
    hass.services.async_register(
        "gnc", "stop_server", stop_gn_server_instance
    )

    # Die Konfiguration über das Frontend ermöglichen
    hass.data["gnc"] = {}

    return True
