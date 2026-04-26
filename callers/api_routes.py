"""API route handlers — call core.process for every endpoint."""

from __future__ import annotations

from core.hub import process


def get_user(user_id: int) -> dict:
    return process({"action": "get_user", "id": user_id})


def list_users(limit: int = 10) -> dict:
    return process({"action": "list_users", "limit": limit})


def create_user(name: str) -> dict:
    return process({"action": "create_user", "name": name})


def update_user(user_id: int, name: str) -> dict:
    return process({"action": "update_user", "id": user_id, "name": name})


def delete_user(user_id: int) -> dict:
    return process({"action": "delete_user", "id": user_id})
