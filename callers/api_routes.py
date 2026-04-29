"""API route handlers — call core.process for every endpoint."""

from __future__ import annotations

from core.hub import process

def get_user(user_id: int) -> dict:
    """Handles the request to retrieve a user by ID.

    Args:
        user_id: The unique identifier of the user to retrieve.

    Returns:
        A dictionary containing the processed response from the hub.
    """
    return process({"action": "get_user", "id": user_id})

def list_users(limit: int = 10) -> dict:
    """Handles the request to list users, optionally applying a limit.

    Args:
        limit: The maximum number of users to return. Defaults to 10.

    Returns:
        A dictionary containing the processed response from the hub.
    """
    return process({"action": "list_users", "limit": limit})

def create_user(name: str) -> dict:
    """Handles the request to create a new user.

    Args:
        name: The desired name for the new user.

    Returns:
        A dictionary containing the processed response from the hub.
    """
    return process({"action": "create_user", "name": name})

def update_user(user_id: int, name: str) -> dict:
    """Handles the request to update an existing user's information.

    Args:
        user_id: The ID of the user to update.
        name: The new name for the user.

    Returns:
        A dictionary containing the processed response from the hub.
    """
    return process({"action": "update_user", "id": user_id, "name": name})

def delete_user(user_id: int) -> dict:
    """Handles the request to delete a user by ID.

    Args:
        user_id: The ID of the user to delete.

    Returns:
        A dictionary containing the processed response from the hub.
    """
    return process({"action": "delete_user", "id": user_id})