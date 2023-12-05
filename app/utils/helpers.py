import datetime

def parse_iso_datetime(iso_string):
    """
    Parses an ISO formatted datetime string to a datetime object.
    """
    try:
        return datetime.datetime.fromisoformat(iso_string)
    except ValueError:
        return None

def format_currency(value, currency="$"):
    """
    Formats a number as a currency string.
    """
    return f"{currency}{value:,.2f}"

# Example usage
# date = parse_iso_datetime('2021-12-31T15:30:00')
# formatted_price = format_currency(1234.56)
