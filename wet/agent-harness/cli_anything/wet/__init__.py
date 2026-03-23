import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wet running')
@cli.command()
def start(): click.echo('wet started')
if __name__ == '__main__': cli()
