import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('OKX status')
@cli.command()
def balance(): click.echo('OKX balance')
if __name__ == '__main__': cli()
