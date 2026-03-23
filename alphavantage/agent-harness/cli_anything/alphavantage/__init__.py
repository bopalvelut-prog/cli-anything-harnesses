import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('alphavantage running')
@cli.command()
def start(): click.echo('alphavantage started')
if __name__ == '__main__': cli()
