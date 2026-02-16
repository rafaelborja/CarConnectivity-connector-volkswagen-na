"""Module for volkswagen vehicle capability class."""

from __future__ import annotations
from typing import TYPE_CHECKING

from enum import IntEnum, StrEnum

from carconnectivity.objects import GenericObject
from carconnectivity.attributes import StringAttribute, BooleanAttribute, DateAttribute, GenericAttribute

if TYPE_CHECKING:
    from typing import Dict, Optional
    from carconnectivity_connectors.volkswagen_na.vehicle import VolkswagenNAVehicle


class Capabilities(GenericObject):
    """
    Represents the capabilities of a Volkswagen vehicle.
    """

    def __init__(self, vehicle: VolkswagenNAVehicle, initialization: Optional[Dict] = None) -> None:
        super().__init__(object_id="capabilities", parent=vehicle, initialization=initialization)
        self.__capabilities: Dict[str, Capability] = {}

    @property
    def capabilities(self) -> Dict[str, Capability]:
        """
        Retrieve the capabilities of the vehicle.

        Returns:
            Dict[str, Capability]: A dictionary of capabilities.
        """
        return self.__capabilities

    def add_capability(self, capability_id: str, capability: Capability) -> None:
        """
        Adds a capability to the Capabilities of the vehicle.

        Args:
            capability_id (str): The unique identifier of the capability.
            capability (Capability): The capability object to be added.

        Returns:
            None
        """
        self.__capabilities[capability_id] = capability

    def remove_capability(self, capability_id: str) -> None:
        """
        Remove a capability from the Capabilities by its capability ID.

        Args:
            capability_id (str): The ID of the capability to be removed.

        Returns:
            None
        """
        if capability_id in self.__capabilities:
            del self.__capabilities[capability_id]

    def clear_capabilities(self) -> None:
        """
        Remove all capabilities from the Capabilities.

        Returns:
            None
        """
        self.__capabilities.clear()

    def get_capability(self, capability_id: str) -> Optional[Capability]:
        """
        Retrieve a capability from the Capabilities by its capability ID.

        Args:
            capability_id (str): The unique identifier of the capability to retrieve.

        Returns:
            Capability: The capability object if found, otherwise None.
        """
        return self.__capabilities.get(capability_id)

    def has_capability(self, capability_id: str, check_status_ok=False) -> bool:
        """
        Check if the Capabilities contains a capability with the specified ID.

        Args:
            capability_id (str): The unique identifier of the capability to check.

        Returns:
            bool: True if the capability exists, otherwise False.
        """
        if check_status_ok:
            if capability_id in self.__capabilities and self.__capabilities[capability_id].enabled:
                capability: Capability = self.__capabilities[capability_id]
                if capability.status.enabled and capability.status.value is not None and len(capability.status.value) > 0:
                    return False
                return True
            return False
        return capability_id in self.__capabilities and self.__capabilities[capability_id].enabled


class Capability(GenericObject):
    """
    Represents a capability of a Volkswagen vehicle.
    """

    def __init__(self, capability_id: str, capabilities: Capabilities, initialization: Optional[Dict] = None) -> None:
        if capabilities is None:
            raise ValueError("Cannot create capability without capabilities")
        if id is None:
            raise ValueError("Capability ID cannot be None")
        super().__init__(object_id=capability_id, parent=capabilities, initialization=initialization)
        self.delay_notifications = True
        self.capability_id = StringAttribute("id", self, capability_id, tags={"connector_custom"}, initialization=self.get_initialization("id"))
        self.expiration_date = DateAttribute("expiration_date", self, tags={"connector_custom"}, initialization=self.get_initialization("expiration_date"))
        self.user_disabling_allowed = BooleanAttribute(
            "user_disabling_allowed", self, tags={"connector_custom"}, initialization=self.get_initialization("user_disabling_allowed")
        )
        self.status = GenericAttribute("status", self, value=[], tags={"connector_custom"}, initialization=self.get_initialization("status"))
        self.enabled = True
        self.delay_notifications = False

    class Status(StrEnum):
        """
        Enum for capability status.
        """

        UNKNOWN = "UNKNOWN"
        DEACTIVATED = "DEACTIVATED"
        INITIALLY_DISABLED = "INITIALLY_DISABLED"
        DISABLED_BY_USER = "DISABLED_BY_USER"
        OFFLINE_MODE = "OFFLINE_MODE"
        WORKSHOP_MODE = "WORKSHOP_MODE"
        MISSING_OPERATION = "MISSING_OPERATION"
        MISSING_SERVICE = "MISSING_SERVICE"
        PLAY_PROTECTION = "PLAY_PROTECTION"
        POWER_BUDGET_REACHED = "POWER_BUDGET_REACHED"
        DEEP_SLEEP = "DEEP_SLEEP"
        LOCATION_DATA_DISABLED = "LOCATION_DATA_DISABLED"
        LICENSE_INACTIVE = "LICENSE_INACTIVE"
        LICENSE_EXPIRED = "LICENSE_EXPIRED"
        MISSING_LICENSE = "MISSING_LICENSE"
        USER_NOT_VERIFIED = "USER_NOT_VERIFIED"
        TERMS_AND_CONDITIONS_NOT_ACCEPTED = "TERMS_AND_CONDITIONS_NOT_ACCEPTED"
        INSUFFICIENT_RIGHTS = "INSUFFICIENT_RIGHTS"
        CONSENT_MISSING = "CONSENT_MISSING"
        LIMITED_FEATURE = "LIMITED_FEATURE"
        AUTH_APP_CERT_ERROR = "AUTH_APP_CERT_ERROR"
        STATUS_UNSUPPORTED = "STATUS_UNSUPPORTED"
        NOT_AVAILABLE = "NOT_AVAILABLE"
        NOT_APPLICABLE = "NOT_APPLICABLE"