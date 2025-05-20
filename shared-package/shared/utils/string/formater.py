import re

def format_to_snake_case(s: str) -> str:
    """
    Convert a given string to snake_case.

    Args:
        s (str): Input string in camelCase, PascalCase, kebab-case, or space separated.

    Returns:
        str: snake_case string.
    """
    s = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
    s = s.replace("-", "_").replace(" ", "_")
    return s


def format_to_camel_case(s: str) -> str:
    """
    Convert a given string to camelCase.

    Args:
        s (str): Input string in snake_case, PascalCase, kebab-case, or space separated.

    Returns:
        str: camelCase string.
    """
    s = s.replace("-", " ").replace("_", " ").title().replace(" ", "")
    return s[0].lower() + s[1:] if s else s


def format_to_pascal_case(s: str) -> str:
    """
    Convert a given string to PascalCase.

    Args:
        s (str): Input string in snake_case, camelCase, kebab-case, or space separated.

    Returns:
        str: PascalCase string.
    """
    s = s.replace("-", " ").replace("_", " ").title().replace(" ", "")
    return s


def format_to_kebab_case(s: str) -> str:
    """
    Convert a given string to kebab-case.

    Args:
        s (str): Input string in camelCase, PascalCase, snake_case, or space separated.

    Returns:
        str: kebab-case string.
    """
    s = re.sub(r'(?<!^)(?=[A-Z])', '-', s).lower()
    s = s.replace("_", "-").replace(" ", "-")
    return s

