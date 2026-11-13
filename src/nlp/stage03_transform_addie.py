"""Analyze comment lengths and email domains.

Author: Addie Gemmell
Date: November 2026
"""

import logging
from typing import Any

import polars as pl


def run_transform(
    json_data: list[dict[str, Any]],
    LOG: logging.Logger,
) -> pl.DataFrame:
    """Transform comments into an analysis-ready dataset."""
    records = []

    for record in json_data:
        records.append(
            {
                "post_id": record["postId"],
                "comment_id": record["id"],
                "name": record["name"],
                "email": record["email"],
                "body": record["body"],
            }
        )

    df = pl.DataFrame(records)

    df = df.with_columns(
        [
            pl.col("body").str.len_chars().alias("comment_length"),
            pl.col("email")
            .str.extract(r"@(.+)$", 1)
            .str.to_lowercase()
            .alias("email_domain"),
            pl.col("email")
            .str.to_lowercase()
            .str.ends_with(".com")
            .alias("is_dot_com"),
        ]
    )

    LOG.info(f"Processed dataset shape: {df.shape}")
    LOG.info(f"DataFrame preview:\n{df.head()}")
    return df
