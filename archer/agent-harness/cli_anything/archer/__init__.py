import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('archer running')
@cli.command()
def start(): click.echo('archer started')
if __name__ == '__main__': cli()
