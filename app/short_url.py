"""short_url.py"""
import string
from zoo_count import counter
from storage import get_full, add_link_db


def int_to_string_encoder(identifier):
    letters = string.ascii_lowercase + string.ascii_uppercase + '0123456789'
    final_identifier = []
    while identifier > 0:
        reminder = identifier % 62
        identifier = identifier // 62
        final_identifier.append(letters[reminder])
    identifier = "".join(final_identifier[::-1])
    return identifier


def add_link(full_url):
    count = int(counter())
    identifier = int_to_string_encoder(count)
    if len(identifier) <= 5:
        identifier = "a" * (5 - len(identifier)) + identifier
        add_link_db(identifier, full_url)
    else:
        return "No Url left"
    return identifier


def get_link(identifier):
    result = get_full(identifier)
    return result
