from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class LoggingInterface(ABC):
    """
    CoreX Interface for Logging.

    This interface standardizes logging operations including logging at various levels,
    configuring logging handlers, and formatting log messages. Implementations can support
    various logging backends (e.g., file logging, console logging, remote logging systems).
    """

    @abstractmethod
    def log_debug(self, message: str, context: Optional[Dict[str, Any]] = None) -> None:
        """
        Log a debug-level message.

        :param message: The debug message.
        :param context: Optional dictionary providing additional context.
        """
        raise NotImplementedError("log_debug must be implemented by subclasses.")

    @abstractmethod
    def log_info(self, message: str, context: Optional[Dict[str, Any]] = None) -> None:
        """
        Log an info-level message.

        :param message: The informational message.
        :param context: Optional dictionary providing additional context.
        """
        raise NotImplementedError("log_info must be implemented by subclasses.")

    @abstractmethod
    def log_warning(self, message: str, context: Optional[Dict[str, Any]] = None) -> None:
        """
        Log a warning-level message.

        :param message: The warning message.
        :param context: Optional dictionary providing additional context.
        """
        raise NotImplementedError("log_warning must be implemented by subclasses.")

    @abstractmethod
    def log_error(self, message: str, context: Optional[Dict[str, Any]] = None) -> None:
        """
        Log an error-level message.

        :param message: The error message.
        :param context: Optional dictionary providing additional context.
        """
        raise NotImplementedError("log_error must be implemented by subclasses.")

    @abstractmethod
    def log_critical(self, message: str, context: Optional[Dict[str, Any]] = None) -> None:
        """
        Log a critical-level message.

        :param message: The critical error message.
        :param context: Optional dictionary providing additional context.
        """
        raise NotImplementedError("log_critical must be implemented by subclasses.")

    @abstractmethod
    def configure(self, config: Dict[str, Any]) -> None:
        """
        Configure the logging system with the given settings.

        :param config: A dictionary containing configuration parameters such as log level,
                       formatters, and handlers.
        """
        raise NotImplementedError("configure must be implemented by subclasses.")

    @abstractmethod
    def add_handler(self, handler: Any) -> None:
        """
        Add a logging handler to the logging system.

        :param handler: A logging handler instance (e.g., file handler, stream handler).
        """
        raise NotImplementedError("add_handler must be implemented by subclasses.")

    @abstractmethod
    def remove_handler(self, handler: Any) -> None:
        """
        Remove a logging handler from the logging system.

        :param handler: The logging handler instance to remove.
        """
        raise NotImplementedError("remove_handler must be implemented by subclasses.")

    @abstractmethod
    def set_log_level(self, level: str) -> None:
        """
        Set the logging level for the system.

        :param level: The log level as a string (e.g., 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
        """
        raise NotImplementedError("set_log_level must be implemented by subclasses.")
