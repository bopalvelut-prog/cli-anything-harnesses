import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('poloniex running')
@cli.command()
def start(): click.echo('poloniex started')
if __name__ == '__main__': cli()
