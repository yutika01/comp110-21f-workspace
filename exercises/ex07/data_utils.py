"""Utility functions."""

__author__ = "730480382"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Product a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(COLUMN_TABLE: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    if num_rows > len(COLUMN_TABLE):
        num_rows = len(COLUMN_TABLE)
    for key in COLUMN_TABLE:
        first_values: list[str] = []
        i: int = 0
        # item: list[str] = []
        while i < num_rows:
            first_values.append(COLUMN_TABLE[key][i])
            i += 1
        result[key] = first_values
    return result


def select(COLUMN_TABLE: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in COLUMN_TABLE:
        for column_name in column_names:
            if column_name == column:
                result[column_name] = COLUMN_TABLE[column_name]
    return result


def concat(TABLE1: dict[str, list[str]], TABLE2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in TABLE1: 
        result[column] = TABLE1[column]
    for second_column in TABLE2: 
        if second_column in result:
            result[second_column] = result[second_column] + TABLE2[second_column]
        else:
            result[second_column] = TABLE2[second_column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Count the frequency of values."""
    result: dict[str, int] = {}
    for item in values: 
        if item in result:
            result[item] += 1
        else: 
            result[item] = 1
    return result