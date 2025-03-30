from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Callable

class ConfigInterface(ABC):
    """
    CoreX Interface for Configuration Management.

    This interface provides a standardized API for loading, retrieving, updating, saving,
    and monitoring configuration data from various sources (e.g., files, environment variables,
    remote services). Implementations should ensure that configuration data is managed in a consistent,
    flexible, and dynamic manner.
    """

    @abstractmethod
    def load(self, source: str) -> None:
        """
        Load configuration data from the specified source.

        :param source: The configuration source (e.g., file path, URL).
        """
        raise NotImplementedError("load must be implemented by subclasses.")

    @abstractmethod
    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """
        Retrieve the value for a given configuration key.

        :param key: The configuration key.
        :param default: The default value if the key is not found.
        :return: The value associated with the key.
        """
        raise NotImplementedError("get must be implemented by subclasses.")

    @abstractmethod
    def set(self, key: str, value: Any) -> None:
        """
        Set or update the value for a given configuration key.

        :param key: The configuration key.
        :param value: The value to set.
        """
        raise NotImplementedError("set must be implemented by subclasses.")

    @abstractmethod
    def delete(self, key: str) -> None:
        """
        Delete the specified configuration key.

        :param key: The configuration key to delete.
        """
        raise NotImplementedError("delete must be implemented by subclasses.")

    @abstractmethod
    def merge(self, config: Dict[str, Any]) -> None:
        """
        Merge the provided configuration dictionary into the current configuration.
        Existing keys will be updated, and new keys will be added.

        :param config: A dictionary of configuration parameters to merge.
        """
        raise NotImplementedError("merge must be implemented by subclasses.")

    @abstractmethod
    def save(self, destination: str) -> None:
        """
        Save the current configuration data to the specified destination.

        :param destination: The target location (e.g., file path) to save the configuration.
        """
        raise NotImplementedError("save must be implemented by subclasses.")

    @abstractmethod
    def reload(self) -> None:
        """
        Reload the configuration data from the original source.
        """
        raise NotImplementedError("reload must be implemented by subclasses.")

    @abstractmethod
    def validate(self) -> bool:
        """
        Validate the current configuration data against predefined rules or a schema.

        :return: True if the configuration is valid, False otherwise.
        """
        raise NotImplementedError("validate must be implemented by subclasses.")

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """
        Return the entire configuration data as a dictionary.

        :return: A dictionary representation of the configuration.
        """
        raise NotImplementedError("to_dict must be implemented by subclasses.")

    @abstractmethod
    def subscribe(self, key: str, callback: Callable[[str, Any], None]) -> None:
        """
        Subscribe to changes for a specific configuration key. When the key's value changes,
        the provided callback will be invoked with the key and its new value.

        :param key: The configuration key to monitor.
        :param callback: A callable that accepts the key and new value.
        """
        raise NotImplementedError("subscribe must be implemented by subclasses.")

    @abstractmethod
    def unsubscribe(self, key: str, callback: Callable[[str, Any], None]) -> None:
        """
        Unsubscribe the given callback from changes to a specific configuration key.

        :param key: The configuration key to stop monitoring.
        :param callback: The callback to remove.
        """
        raise NotImplementedError("unsubscribe must be implemented by subclasses.")

    @abstractmethod
    def watch(self) -> None:
        """
        Watch the configuration source for changes and automatically reload the configuration.
        This method should be implemented if dynamic configuration reloading is supported.
        """
        raise NotImplementedError("watch must be implemented by subclasses.")

    @abstractmethod
    def export_to_json(self) -> str:
        """
        Export the current configuration to a JSON formatted string.

        :return: A JSON string representation of the configuration.
        """
        raise NotImplementedError("export_to_json must be implemented by subclasses.")

    @abstractmethod
    def import_from_dict(self, config_dict: Dict[str, Any]) -> None:
        """
        Import configuration data from a dictionary and replace the current configuration.

        :param config_dict: A dictionary containing configuration data.
        """
        raise NotImplementedError("import_from_dict must be implemented by subclasses.")
