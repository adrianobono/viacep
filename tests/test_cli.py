import pytest
from click.testing import CliRunner
from viacep.cli import main


class TestCLI:
    @pytest.fixture
    def runner(self):
        return CliRunner()

    def test_search_success(self, runner, mock_successful_cep_lookup):
        result = runner.invoke(main, ["search", "01001000"])
        assert result.exit_code == 0
        assert "Praça da Sé" in result.output
        assert "São Paulo" in result.output

    def test_search_invalid_cep(self, runner):
        result = runner.invoke(main, ["search", "invalid"])
        assert result.exit_code == 1
        assert "CEP must contain exactly 8 digits" in result.output

    def test_search_not_found(self, runner, mock_cep_not_found):
        result = runner.invoke(main, ["search", "00000000"])
        assert result.exit_code == 1
        assert "CEP 00000000 not found" in result.output