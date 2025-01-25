import logging

from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the GN Server integration."""
    _LOGGER.info("GN Server Integration has been set up!")
    return True
