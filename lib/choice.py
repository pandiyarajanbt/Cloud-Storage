def choices_the_options(cls):
    return [(tag.value, tag.name.replace("_", " ").title()) for tag in cls]