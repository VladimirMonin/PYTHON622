"""
Урок 34 - Датаклассы в Python

Датаклассы в Python специальные классы которые являются своим своего рода синтаксическим сахаром Они упрощают создание обычных классов и избавляют нас от необходимости писать некоторые вещи Например они автоматически создают инициализатор а также автоматически описывают некоторые специальные методы
"""

from dataclasses import dataclass, field, asdict


@dataclass
class Config:
    app_name: str
    app_version: str
    model: str
    polza_api_key: str = field(default="", repr=False)
    debug_mode: bool = False
    default_config: dict = field(
        default_factory=lambda: {
            "app_name": "Детектор сосисок",
            "app_version": "0.0.1",
            "model": "glm-sausage-flash-4.1",
            "polza_api_key": "13sfsdflajfjlaf",
            "debug_mode": True,
        },
        init=False,
        repr=False,
        compare=False,
    )

