#!/usr/bin/env python3
"""
fetch.py.

Script for reading the configuration and displaying current values.
This script is designed to read a YAML configuration file
and validate its contents.
It uses the Pydantic library for data validation
and Click for command-line interface.
"""

from pathlib import Path

import click
import yaml
from pydantic import BaseModel, ValidationError


# Configuration description
class AppConfig(BaseModel):
    """
    Configuration for the application.

    Attributes:
        db_path (str): Path to the SQLite database.
        llm_endpoint (str): Endpoint for the LLM service.
        feeds (list[str]): List of feed URLs.
    """

    db_path: str = "jobs.sqlite"
    llm_endpoint: str
    feeds: list[str] = []


# Loading and validating the YAML config
def load_config(path: Path) -> AppConfig:
    """Load and validate the YAML configuration file.

    Args:
        path (Path): Path to the YAML configuration file.
    Returns:
        AppConfig: An instance of AppConfig with the loaded configuration.
    Raises:
        click.ClickException: If the file cannot be read
        or the YAML is invalid.
    """
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        raise click.ClickException(f"Error parsing YAML: {e}")
    try:
        return AppConfig(**data)
    except ValidationError as e:
        raise click.ClickException(f"Invalid configuration:\n{e}")


@click.command()
@click.option(
    "--config",
    "-c",
    type=click.Path(exists=True),
    required=True,
    help="Path to the YAML config (e.g., config/default.yaml)",
)
def fetch(config):
    """Script for reading the configuration and displaying current values."""
    cfg = load_config(Path(config))
    click.echo(f"Database path: {cfg.db_path}")
    click.echo(f"LLM endpoint: {cfg.llm_endpoint}")
    click.echo(f"Feeds: {cfg.feeds}")


if __name__ == "__main__":
    fetch()
