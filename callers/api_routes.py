"""API route handlers — call core.process for every endpoint."""

from __future__ import annotations

from core.hub import process

def get_user(user_id: int) -> dict:
    """Handles the request to retrieve a user by ID.

    Parameters
    ----------
    user_id : int
        The unique identifier of the user to fetch.

    Returns
    -------
    dict
        The processed response containing user data.
    """
    return process({"action": "get_user", "id": user_id})

def list_users(limit: int = 10) -> dict:
    """Handles the request to list users, optionally applying a limit.

    Parameters
    ----------
    limit : int, optional
        The maximum number of users to return (default is 10).

    Returns
    -------
    dict
        The processed response containing a list of users.
    """
    return process({"action": "list_users", "limit": limit})

def create_user(name: str) -> dict:
    """Handles the request to create a new user.

    Parameters
    ----------
    name : str
        The desired name for the new user.

    Returns
    -------
    dict
        The processed response confirming user creation.
    """
    return process({"action": "create_user", "name": name})

def update_user(user_id: int, name: str) -> dict:
    """Handles the request to update an existing user's information.

    Parameters
    ----------
    user_id : int
        The unique identifier of the user to update.
    name : str
        The new name for the user.

    Returns
    -------
    dict
        The processed response confirming the update.
    """
    return process({"action": "update_user", "id": user_id, "name": name})

def delete_user(user_id: int) -> dict:
    """Handles the request to delete a user by ID.

    Parameters
    ----------
    user_id : int
        The unique identifier of the user to delete.

    Returns
    -------
    dict
        The processed response confirming the deletion.
    """
    return process({"action": "delete_user", "id": user_id})