from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PORT
import voluptuous as vol
import logging

_LOGGER = logging.getLogger(__name__)

class GncConfigFlow(config_entries.ConfigFlow):
    """Handle a config flow for GNC."""
    
    VERSION = 1
    
    def __init__(self):
        self.host = None
        self.port = None

    async def async_step_user(self, user_input=None):
        """Handle the user input for the config flow."""
        if user_input is not None:
            # Validating user input and saving it
            self.host = user_input[CONF_HOST]
            self.port = user_input[CONF_PORT]
            
            # Store the user input (host and port) and return the result
            return self.async_create_entry(
                title=f"{self.host}:{self.port}",
                data={CONF_HOST: self.host, CONF_PORT: self.port}
            )
        
        # If no input, show the form to the user
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_HOST): str,
                vol.Required(CONF_PORT, default=6990): int
            })
        )
