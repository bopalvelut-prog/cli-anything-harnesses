import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('great running')
@cli.command()
def start(): click.echo('great started')
if __name__ == '__main__': cli()
