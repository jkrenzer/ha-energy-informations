"""HA Energy Informations integration."""

from homeassistant.core import HomeAssistant

DOMAIN = "ha_energy_informations"
__version__ = "0.1.0"


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the integration."""
    hass.data.setdefault(DOMAIN, {})
    return True
