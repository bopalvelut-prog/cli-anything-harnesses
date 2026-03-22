import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Binance status')
@cli.command()
def balance(): click.echo('Binance balance')
if __name__ == '__main__': cli()
