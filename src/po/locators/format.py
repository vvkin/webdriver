def format_locator(locator: tuple[str, str], *args) -> tuple[str, str]:
    by, path = locator
    return (by, path.format(*args))
