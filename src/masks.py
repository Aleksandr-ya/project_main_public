def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    card_number_str = str(card_number)
    return card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]


def get_mask_account(account: int) -> str:
    """Функция маскировки номера банковского счета"""
    return "**" + str(account)[-4:]


# print(get_mask_card_number(1234567890123456))
# print(get_mask_account(12345678901234567890))
