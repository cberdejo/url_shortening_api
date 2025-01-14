def validateUrlIsPresentAndValid(url):
    if not url:
        return False
    if not isinstance(url, str):
        return False
    # future validations
    return True


example_api = "124567"


def checkAuhtorization(api_key):
    if api_key == example_api:
        return True
    return False
