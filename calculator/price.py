import logging
logger = logging.getLogger(__name__)

def apply_discount(price: float, discount_percent: float) -> float:
    logger.debug(
        "Applying discount: price=%s, discount_percent=%s",
        price,
        discount_percent,
    )

    if price < 0:
        raise ValueError("Price cannot be negative")
    
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    
    result = price * (1 - discount_percent / 100)

    logger.info(
        "Discount applied successfully: original=%s, discount=%s, result=%s",
        price,
        discount_percent,
        result,
    )

    return result


def add_vat(price: float, vat_percent: float) -> float:
    logger.debug(
        "Adding VAT: price=%s, vat_percent=%s",
        price,
        vat_percent,
    )

    if vat_percent < 0:
        logger.error("Negative VAT detected: %s", vat_percent)
        raise ValueError("VAT cannot be negative")

    result = price * (1 + vat_percent / 100)

    logger.info(
        "VAT added successfully: original=%s, vat=%s, result=%s",
        price,
        vat_percent,
        result,
    )

    return result