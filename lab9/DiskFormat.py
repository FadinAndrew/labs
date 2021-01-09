u"""Модуль класса типов форматов диска."""

from enum import Enum


class DiskFormat(Enum):
    u"""Класс типов форматов дисков."""

    DVD = 1
    MPEG4 = 2
    BLURAY = 3
    HD_DVD = 4
