import logging
import subprocess
import os

_LOGGER = logging.getLogger(__name__)

DOMAIN = "gnc"

def setup(hass, config):
    """Set up the GNC integration."""
    _LOGGER.info("Setting up GNC integration...")

    # Pfad zur JAR-Datei
    jar_path = os.path.join(
        hass.config.path("custom_components"), DOMAIN, "gn_server.jar"
    )

    if not os.path.isfile(jar_path):
        _LOGGER.error("gn_server.jar not found at %s", jar_path)
        return False

    _LOGGER.info("Found gn_server.jar at %s", jar_path)

    # Versuche, den Server zu starten
    try:
        command = f"java -jar {jar_path}"
        _LOGGER.info("Executing command: %s", command)
        subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        _LOGGER.info("GNC server started successfully.")
    except Exception as e:
        _LOGGER.error("Failed to start GNC server: %s", str(e))
        return False

    return True
