from django import template

register = template.Library()

census = [
    'Агентство',
    'Политик',
    'Политика',
    'Политике',
    'Новации',
    'Инцидентов'
]


@register.filter()
def censor(text):
    """
    Фильтр для цензуры

    """
    if not isinstance(text, str):
        raise TypeError()

    for word in text.split():
        if word.title() in census:
            text = text.replace(word, f"{word[0]}{'*' * (len(word) - 2)}{word[-1]}")
    return text