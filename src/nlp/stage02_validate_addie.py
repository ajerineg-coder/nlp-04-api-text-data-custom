"""Validate comment records.

Author: Addie Gemmell
Date: November 2026
"""

import logging
from typing import Any


def run_validate(
    json_data: Any,
    LOG: logging.Logger,
) -> list[dict]:
    """Validate the structure and fields of comment records."""
    if not isinstance(json_data, list):
        raise TypeError("Expected a list of comments.")

    if not json_data:
        raise ValueError("No comments found.")

    expected = {
        "postId": int,
        "id": int,
        "name": str,
        "email": str,
        "body": str,
    }

    for record in json_data:
        if not isinstance(record, dict):
            raise TypeError("Expected a dictionary.")

        for field, field_type in expected.items():
            if field not in record or not isinstance(record[field], field_type):
                raise ValueError(f"Invalid field: {field}")

    LOG.info(f"Fields: {list(json_data[0].keys())}")
    LOG.info(f"Validated {len(json_data)} comments.")
    return json_data
