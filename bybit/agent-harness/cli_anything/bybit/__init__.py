import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Bybit status')
@cli.command()
def balance(): click.echo('Bybit balance')
if __name__ == '__main__': cli()
