from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class SecurityInterface(ABC):
    """
    CoreX Interface for Security.
    
    This interface standardizes security operations such as authentication, 
    authorization, token management, and encryption. Implementations may vary 
    based on the underlying authentication mechanism (e.g., OAuth2, LDAP, JWT, etc.).
    """

    @abstractmethod
    def authenticate(self, credentials: Dict[str, Any]) -> Any:
        """
        Authenticate a user using the provided credentials.
        
        :param credentials: A dictionary containing authentication data (e.g., username and password).
        :return: An object representing the authenticated user/session.
        """
        raise NotImplementedError("authenticate must be implemented by subclasses.")

    @abstractmethod
    def authorize(self, user: Any, action: str, resource: str) -> bool:
        """
        Authorize a specific action for a given user on a resource.
        
        :param user: The user object returned from authenticate.
        :param action: The action that the user is attempting (e.g., 'read', 'write').
        :param resource: The target resource (e.g., a file, database record, API endpoint).
        :return: True if the action is authorized, False otherwise.
        """
        raise NotImplementedError("authorize must be implemented by subclasses.")

    @abstractmethod
    def generate_token(self, user: Any, **kwargs) -> str:
        """
        Generate a security token for the given user.
        
        :param user: The user object for whom to generate the token.
        :param kwargs: Additional parameters for token generation.
        :return: A string representing the generated token.
        """
        raise NotImplementedError("generate_token must be implemented by subclasses.")

    @abstractmethod
    def validate_token(self, token: str) -> Optional[Any]:
        """
        Validate the provided token.
        
        :param token: The security token to validate.
        :return: The user/session object if the token is valid; otherwise, None.
        """
        raise NotImplementedError("validate_token must be implemented by subclasses.")

    @abstractmethod
    def revoke_token(self, token: str) -> None:
        """
        Revoke an existing token, rendering it invalid.
        
        :param token: The token to revoke.
        """
        raise NotImplementedError("revoke_token must be implemented by subclasses.")

    @abstractmethod
    def encrypt(self, data: bytes, key: bytes) -> bytes:
        """
        Encrypt data using the specified key.
        
        :param data: The plaintext data to encrypt.
        :param key: The encryption key.
        :return: The encrypted data as bytes.
        """
        raise NotImplementedError("encrypt must be implemented by subclasses.")

    @abstractmethod
    def decrypt(self, data: bytes, key: bytes) -> bytes:
        """
        Decrypt data using the specified key.
        
        :param data: The encrypted data to decrypt.
        :param key: The decryption key.
        :return: The decrypted data as bytes.
        """
        raise NotImplementedError("decrypt must be implemented by subclasses.")
