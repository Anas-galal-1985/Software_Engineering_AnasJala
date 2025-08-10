from django import template

register = template.Library()

@register.filter(name='arabic_to_english_numbers')
def arabic_to_english_numbers(value):
    """
    يحول الأرقام العربية ٠١٢٣٤٥٦٧٨٩ إلى الأرقام الإنجليزية 0123456789 في النص
    """
    if not isinstance(value, str):
        return value

    arabic_nums = '٠١٢٣٤٥٦٧٨٩'
    english_nums = '0123456789'
    translation_table = str.maketrans(arabic_nums, english_nums)
    return value.translate(translation_table)