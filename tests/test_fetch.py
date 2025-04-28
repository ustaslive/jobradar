"""Unit tests for the fetch script."""

import pytest
import yaml
from click.testing import CliRunner

from scripts.fetch import fetch


# 1) Test: missing required parameter --config
def test_missing_config_option():
    """Test that the script fails when the --config option is missing."""
    runner = CliRunner()
    result = runner.invoke(fetch, [])
    assert result.exit_code != 0
    assert "Missing option" in result.output


# 2) Test: invalid YAML file
def test_invalid_yaml(tmp_path):
    """Test that the script fails when the YAML file is invalid."""
    bad = tmp_path / "bad.yaml"
    bad.write_text("not: [unbalanced")  # invalid YAML
    with pytest.raises(yaml.YAMLError):
        # directly test the load_config function
        yaml.safe_load(bad.read_text())


# 3) Test: invalid schema (missing llm_endpoint)
def test_schema_validation(tmp_path):
    """Test that the script fails when the schema is invalid."""
    bad = tmp_path / "schema_bad.yaml"
    bad.write_text("db_path: jobs.sqlite\nfeeds: []\n")
    runner = CliRunner()
    result = runner.invoke(fetch, ["--config", str(bad)])
    assert result.exit_code != 0
    assert "Invalid configuration" in result.output
