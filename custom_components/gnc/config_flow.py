import logging
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult

_LOGGER = logging.getLogger(__name__)

class GncConfigFlow(config_entries.ConfigFlow, domain="gnc"):
    """Handle a config flow for GNC Server."""

    def __init__(self):
        """Initialize the GNC config flow."""
        self.ports = []

    async def async_step_user(self, user_input=None):
        """Handle the initial user input."""
        if user_input is not None:
            self.ports = user_input["ports"]
            return self.async_create_entry(
                title="GNC Server", data={"ports": self.ports}
            )
        return self.async_show_form(
            step_id="user", data_schema=self._get_data_schema()
        )

    def _get_data_schema(self):
        """Return the data schema for the form."""
        import voluptuous as vol
        from homeassistant.helpers import config_validation as cv

        return vol.Schema(
            {
                vol.Required("ports"): cv.ensure_list,
            }
        )
