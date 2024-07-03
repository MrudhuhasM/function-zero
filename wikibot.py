import click
from mylib.bot import scrape


@click.command()
@click.option('--name', default='Vizag', help='Name of the city to scrape')
@click.option('--length', default=2, help='Number of sentences to scrape')
def cli(name,length):
    result = scrape(name, length)
    click.echo(click.style(result, fg='green'))

if __name__ == '__main__':
    cli("Vizag", 2)



