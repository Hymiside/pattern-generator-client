from typing import Dict

import requests


def user_status(user_id: int) -> Dict[str, str]:
    """Метод проверяет существует ли уже такой пользователь"""
    """url = ""
    data = {
        "user_id": user_id
    }
    response = requests.post(url, json=data)

    match response.status_code:
        case 500:
            return {"status": "error"}
        case _:
            return response.json()"""

    return {"status": "user does not exist"}


def get_balance(user_id: int) -> Dict[str, str]:
    """Метод возвращает баланс пользователя"""

    """url = ""
        data = {
            "user_id": user_id
        }
        response = requests.post(url, json=data)

        match response.status_code:
            case 500:
                return {
                    "status": "error",
                    "balance": "-"
                }
            case _:
                return response.json()"""

    return {
        "status": "ok",
        "balance": "500"
    }
