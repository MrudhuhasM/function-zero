from mylib.bot import scrape
from click.testing import CliRunner
from wikibot import cli


def test_scrape():
    assert "Mumbai" in scrape("Mumbai")

def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ['--name', 'Mumbai', '--length', 3])
    assert 'Mumbai' in result.output
    assert result.exit_code == 0
