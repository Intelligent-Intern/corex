from abc import ABC, abstractmethod
from typing import Any, Dict

class LifecycleInterface(ABC):
    """
    CoreX Interface for Lifecycle Management.

    This interface standardizes lifecycle operations for applications or services,
    including initialization, startup, shutdown, restart, and cleanup. Implementations
    should provide concrete logic for handling various lifecycle phases.
    """

    @abstractmethod
    def initialize(self, config: Dict[str, Any]) -> None:
        """
        Initialize the service or application with the given configuration.

        :param config: A dictionary of configuration parameters.
        """
        raise NotImplementedError("initialize must be implemented by subclasses.")

    @abstractmethod
    def start(self) -> None:
        """
        Start the service or application.
        """
        raise NotImplementedError("start must be implemented by subclasses.")

    @abstractmethod
    def stop(self) -> None:
        """
        Stop the service or application.
        """
        raise NotImplementedError("stop must be implemented by subclasses.")

    @abstractmethod
    def restart(self) -> None:
        """
        Restart the service or application.
        """
        raise NotImplementedError("restart must be implemented by subclasses.")

    @abstractmethod
    def shutdown(self) -> None:
        """
        Shutdown the service or application gracefully.
        """
        raise NotImplementedError("shutdown must be implemented by subclasses.")

    @abstractmethod
    def health_check(self) -> bool:
        """
        Perform a health check to verify that the service or application is functioning properly.

        :return: True if healthy, False otherwise.
        """
        raise NotImplementedError("health_check must be implemented by subclasses.")

    @abstractmethod
    def cleanup(self) -> None:
        """
        Clean up resources and perform any necessary finalization tasks.
        """
        raise NotImplementedError("cleanup must be implemented by subclasses.")
