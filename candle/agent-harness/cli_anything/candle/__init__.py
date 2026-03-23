import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('candle running')
@cli.command()
def start(): click.echo('candle started')
if __name__ == '__main__': cli()
