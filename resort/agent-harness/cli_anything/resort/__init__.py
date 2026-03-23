import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('resort running')
@cli.command()
def start(): click.echo('resort started')
if __name__ == '__main__': cli()
