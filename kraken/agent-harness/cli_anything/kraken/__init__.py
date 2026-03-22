import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Kraken status')
@cli.command()
def balance(): click.echo('Kraken balance')
if __name__ == '__main__': cli()
