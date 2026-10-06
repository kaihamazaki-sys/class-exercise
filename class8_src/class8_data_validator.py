import logging

logger = logging.getLogger(__name__)

def require_columns(df, required_columns):
    """Check that all required columns exist."""
    # TODO 2:
    # Check if any of the configured columns (list) are missing from df.
    # If any are missing, log an ERROR and raise ValueError.
    # Log an INFO.
    # Return the DataFrame.
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        logger.error(f"Missing Columns: {', '.join(missing_columns)}")
        raise ValueError(f"Missing columns: {missing_columns}")
    logger.info(f"All required columns present: {', '.join(required_columns)}")
    return df

            