import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Coinbase status')
@cli.command()
def balance(): click.echo('Coinbase balance')
if __name__ == '__main__': cli()
