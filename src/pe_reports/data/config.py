"""Configuration to connect to a PostgreSQL database."""

# Standard Python Libraries
from configparser import ConfigParser
from importlib.resources import files

REPORT_DB_CONFIG = files("pe_reports").joinpath("data/dbconfig.config")


def config(filename=REPORT_DB_CONFIG, section="postgres"):
    """Parse Postgres configuration details from database configuration file."""
    parser = ConfigParser()

    parser.read(filename, encoding="utf-8")

    if not parser.has_section(section):
        raise Exception(f"Section {section} not found in {filename}")

    return dict(parser.items(section))
