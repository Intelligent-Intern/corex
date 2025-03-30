from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, List

class AuthInterface(ABC):
    """
    CoreX Interface for Authentication.

    This interface standardizes operations for user authentication and session management.
    Implementations should provide a unified API for tasks such as user registration, login,
    logout, token management, password management, multi-factor authentication (MFA), and
    role/permission checks. This enables secure and consistent authentication flows across
    various applications and services.
    """

    # User Registration and Account Management
    @abstractmethod
    def register_user(self, user_data: Dict[str, Any]) -> Any:
        """
        Register a new user with the system.

        :param user_data: A dictionary containing user information (e.g., username, email, password).
        :return: An object representing the registered user or a confirmation message.
        """
        raise NotImplementedError("register_user must be implemented by subclasses.")

    @abstractmethod
    def get_user_info(self, user_id: str) -> Dict[str, Any]:
        """
        Retrieve information about a user.

        :param user_id: Unique identifier for the user.
        :return: A dictionary containing user details (e.g., profile info, roles, permissions).
        """
        raise NotImplementedError("get_user_info must be implemented by subclasses.")

    @abstractmethod
    def set_user_role(self, user_id: str, role: str) -> None:
        """
        Assign a role to a user.

        :param user_id: Unique identifier for the user.
        :param role: The role to assign (e.g., 'admin', 'user', 'editor').
        """
        raise NotImplementedError("set_user_role must be implemented by subclasses.")

    # Login, Logout, and Session Management
    @abstractmethod
    def login(self, username: str, password: str) -> str:
        """
        Authenticate the user and establish a session.

        :param username: The user's username.
        :param password: The user's password.
        :return: A session token (e.g., JWT) upon successful authentication.
        """
        raise NotImplementedError("login must be implemented by subclasses.")

    @abstractmethod
    def logout(self, token: str) -> None:
        """
        Terminate a user's session and invalidate the token.

        :param token: The session token to be invalidated.
        """
        raise NotImplementedError("logout must be implemented by subclasses.")

    @abstractmethod
    def is_authenticated(self, token: str) -> bool:
        """
        Check whether a given session token is valid and corresponds to an authenticated user.

        :param token: The session token.
        :return: True if the token is valid, False otherwise.
        """
        raise NotImplementedError("is_authenticated must be implemented by subclasses.")

    # Token Management
    @abstractmethod
    def generate_token(self, user_id: str) -> str:
        """
        Generate an authentication token for the user.

        :param user_id: Unique identifier for the user.
        :return: A token string (e.g., JWT).
        """
        raise NotImplementedError("generate_token must be implemented by subclasses.")

    @abstractmethod
    def validate_token(self, token: str) -> Optional[Dict[str, Any]]:
        """
        Validate a token and return associated user information if valid.

        :param token: The token to validate.
        :return: A dictionary of user claims if the token is valid; otherwise, None.
        """
        raise NotImplementedError("validate_token must be implemented by subclasses.")

    @abstractmethod
    def refresh_token(self, token: str) -> str:
        """
        Refresh an existing token, extending its validity.

        :param token: The token to refresh.
        :return: A new token with extended validity.
        """
        raise NotImplementedError("refresh_token must be implemented by subclasses.")

    @abstractmethod
    def revoke_token(self, token: str) -> None:
        """
        Revoke a token so that it can no longer be used for authentication.

        :param token: The token to revoke.
        """
        raise NotImplementedError("revoke_token must be implemented by subclasses.")

    # Password Management
    @abstractmethod
    def change_password(self, user_id: str, old_password: str, new_password: str) -> bool:
        """
        Change a user's password.

        :param user_id: Unique identifier for the user.
        :param old_password: The current password.
        :param new_password: The new password to set.
        :return: True if the password was changed successfully, False otherwise.
        """
        raise NotImplementedError("change_password must be implemented by subclasses.")

    @abstractmethod
    def reset_password(self, email: str) -> bool:
        """
        Initiate a password reset process for the user.

        :param email: The email address associated with the user's account.
        :return: True if the reset process was initiated successfully, False otherwise.
        """
        raise NotImplementedError("reset_password must be implemented by subclasses.")

    # Multi-Factor Authentication (MFA)
    @abstractmethod
    def setup_mfa(self, user_id: str) -> Any:
        """
        Setup multi-factor authentication for a user (e.g., generate and associate an MFA secret).

        :param user_id: Unique identifier for the user.
        :return: Information necessary for MFA setup (e.g., QR code data, secret key).
        """
        raise NotImplementedError("setup_mfa must be implemented by subclasses.")

    @abstractmethod
    def verify_mfa(self, user_id: str, mfa_code: str) -> bool:
        """
        Verify the MFA code provided by the user.

        :param user_id: Unique identifier for the user.
        :param mfa_code: The MFA code to verify.
        :return: True if the MFA code is correct, False otherwise.
        """
        raise NotImplementedError("verify_mfa must be implemented by subclasses.")

    # Authorization and Permissions
    @abstractmethod
    def check_permission(self, user_id: str, permission: str) -> bool:
        """
        Check whether a user has a specific permission.

        :param user_id: Unique identifier for the user.
        :param permission: The permission to check (e.g., 'read', 'write', 'delete').
        :return: True if the user has the permission, False otherwise.
        """
        raise NotImplementedError("check_permission must be implemented by subclasses.")
