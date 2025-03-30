from abc import ABC, abstractmethod
from typing import Any, Optional, List

class CacheInterface(ABC):
    """
    CoreX Interface for Cache.

    This interface standardizes cache operations for storing, retrieving, and managing cached data.
    Implementations can support various caching backends (e.g., Redis, Memcached, in-memory caches) and
    must adhere to this interface to provide consistent caching functionality across applications.
    """

    @abstractmethod
    def set(self, key: str, value: Any, expire: Optional[int] = None) -> None:
        """
        Store a value in the cache with an optional expiration time.

        :param key: The cache key.
        :param value: The value to store.
        :param expire: Optional expiration time in seconds.
        """
        raise NotImplementedError("set must be implemented by subclasses.")

    @abstractmethod
    def get(self, key: str) -> Any:
        """
        Retrieve a value from the cache.

        :param key: The cache key.
        :return: The value associated with the key, or None if not found.
        """
        raise NotImplementedError("get must be implemented by subclasses.")

    @abstractmethod
    def delete(self, key: str) -> None:
        """
        Delete a value from the cache.

        :param key: The cache key to delete.
        """
        raise NotImplementedError("delete must be implemented by subclasses.")

    @abstractmethod
    def exists(self, key: str) -> bool:
        """
        Check if a key exists in the cache.

        :param key: The cache key.
        :return: True if the key exists, False otherwise.
        """
        raise NotImplementedError("exists must be implemented by subclasses.")

    @abstractmethod
    def clear(self) -> None:
        """
        Clear all entries from the cache.
        """
        raise NotImplementedError("clear must be implemented by subclasses.")

    @abstractmethod
    def increment(self, key: str, delta: int = 1) -> int:
        """
        Increment a numeric value in the cache.

        :param key: The cache key.
        :param delta: The amount to increment by.
        :return: The new value after incrementing.
        """
        raise NotImplementedError("increment must be implemented by subclasses.")

    @abstractmethod
    def decrement(self, key: str, delta: int = 1) -> int:
        """
        Decrement a numeric value in the cache.

        :param key: The cache key.
        :param delta: The amount to decrement by.
        :return: The new value after decrementing.
        """
        raise NotImplementedError("decrement must be implemented by subclasses.")

    @abstractmethod
    def keys(self, pattern: str) -> List[str]:
        """
        Retrieve all cache keys matching the specified pattern.

        :param pattern: A pattern to match keys (e.g., "user:*").
        :return: A list of matching keys.
        """
        raise NotImplementedError("keys must be implemented by subclasses.")

    @abstractmethod
    def expire(self, key: str, time: int) -> bool:
        """
        Set an expiration time on a cache key.

        :param key: The cache key.
        :param time: Expiration time in seconds.
        :return: True if the timeout was set, False otherwise.
        """
        raise NotImplementedError("expire must be implemented by subclasses.")

    @abstractmethod
    def ttl(self, key: str) -> Optional[int]:
        """
        Get the time-to-live (TTL) of a cache key.

        :param key: The cache key.
        :return: The remaining time-to-live in seconds, or None if the key does not exist or has no expiration.
        """
        raise NotImplementedError("ttl must be implemented by subclasses.")
