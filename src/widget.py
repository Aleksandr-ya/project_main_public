import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_number: str) -> str:
    """Функция принимает строку, содержащую тип и номер карты или счета
    и возвращает строку с замаскированным номером"""

    # Получим номер карты или счёта
    number = int(re.findall(r"\d+", name_number)[-1])

    # Маскируем номер при помощи функций get_mask_card_number и get_mask_account
    if len(str(number)) == 16:
        mask_number = get_mask_card_number(number)
    elif len(str(number)) == 20:
        mask_number = get_mask_account(number)
    else:
        return "Неверный формат"

    return name_number[0 : -len(str(number))] + mask_number


def get_date(date_original: str) -> str:
    """Функция принимает на вход строку с датой в формате  'ГГГГ-ММ-ДД...'
    и возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""

    return f"{date_original[8:10]}.{date_original[5:7]}.{date_original[0:4]}"


# print(mask_account_card("МИР 1234567890123456"))
# print(mask_account_card("Счет 73654108430135874305"))
# print(get_date("2024-03-11T02:26:18.671407"))
