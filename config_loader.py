import os
import yaml
import importlib
from typing import Any, Dict, Optional, Type


DEFAULT_GLOBAL_CONFIG_PATH = os.path.expanduser("~/.corex.yaml")


def _load_yaml_config(path: Optional[str]) -> Dict[str, Any]:
    """
    Load and parse YAML config file. Falls back to global config if path is None.
    """
    target_path = path or DEFAULT_GLOBAL_CONFIG_PATH
    if not os.path.exists(target_path):
        raise FileNotFoundError(f"CoreX config not found: {target_path}")
    with open(target_path, "r") as f:
        return yaml.safe_load(f)


def _load_class(import_path: str) -> Any:
    """
    Dynamically import a class given its full import path.
    Example: "corex_storage_minio.handler.MinioHandler"
    """
    module_path, class_name = import_path.rsplit(".", 1)
    module = importlib.import_module(module_path)
    return getattr(module, class_name)


def _validate_interface(instance: Any, interface: Optional[Type]) -> None:
    """
    Optionally validate that the loaded backend instance implements a specific interface.
    """
    if interface and not isinstance(instance, interface):
        raise TypeError(f"Loaded class does not implement required interface: {interface.__name__}")


def load_backend(section: str, config_path: Optional[str] = None, interface: Optional[Type] = None) -> Any:
    """
    Load any backend (e.g. storage, messaging, ai_nlp) from YAML config.

    Args:
        section: e.g. "storage", "messaging", "ai_nlp"
        config_path: optional path to a config file
        interface: optional class or ABC for type validation

    Returns:
        Instantiated backend object
    """
    config = _load_yaml_config(config_path)
    section_conf = config.get(section)
    if not section_conf:
        raise ValueError(f"Missing config section: '{section}'")

    class_path = section_conf["backend"]
    init_args = section_conf.get("init_args", {})

    cls = _load_class(class_path)
    instance = cls(**init_args)

    _validate_interface(instance, interface)
    return instance


# Convenience wrappers
def load_storage_backend(config_path: Optional[str] = None) -> Any:
    from corex.interfaces.storage_interface import StorageInterface
    return load_backend("storage", config_path, interface=StorageInterface)

def load_messaging_backend(config_path: Optional[str] = None) -> Any:
    from corex.interfaces.messaging_interface import MessagingInterface
    return load_backend("messaging", config_path, interface=MessagingInterface)

def load_cache_backend(config_path: Optional[str] = None) -> Any:
    from corex.interfaces.cache_interface import CacheInterface
    return load_backend("cache", config_path, interface=CacheInterface)

def load_ai_backend(category: str, config_path: Optional[str] = None) -> Any:
    """
    Example: load_ai_backend("ai_nlp")
    """
    return load_backend(category, config_path)
