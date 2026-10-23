from dataclasses import dataclass
from pathlib import Path
from uuid import uuid4


@dataclass(frozen=True)
class User:
    email: str
    username: str
    password: str = "QaSprint9!2026Secure"
    first_name: str = "Иван"
    last_name: str = "Тестовый"

    @classmethod
    def unique(cls):
        suffix = uuid4().hex[:16]
        email = f"sprint9_{suffix}@example.com"
        return cls(email=email, username=email)


@dataclass(frozen=True)
class Recipe:
    name: str
    ingredient: str = "абрикосы"
    amount: str = "100"
    cooking_time: str = "15"
    description: str = "Промыть абрикосы, нарезать и подать."
    image: Path = Path(__file__).resolve().parent / "assets" / "recipe.png"

    @classmethod
    def unique(cls):
        return cls(name=f"Абрикосовый десерт {uuid4().hex[:10]}")
