import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('plumber running')
@cli.command()
def start(): click.echo('plumber started')
if __name__ == '__main__': cli()
