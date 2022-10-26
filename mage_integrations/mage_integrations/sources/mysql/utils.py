from mage_integrations.sources.constants import (
    COLUMN_TYPE_BOOLEAN,
    COLUMN_TYPE_INTEGER,
    COLUMN_TYPE_NUMBER,
    COLUMN_TYPE_OBJECT,
)


def column_type_mapping(column_type: str) -> str:
    if COLUMN_TYPE_BOOLEAN == column_type:
        return 'BOOL'
    elif COLUMN_TYPE_INTEGER == column_type:
        return 'UNSIGNED INTEGER'
    elif COLUMN_TYPE_NUMBER == column_type:
        return 'DECIMAL'
    elif COLUMN_TYPE_OBJECT == column_type:
        return 'TEXT'

    return 'CHAR'