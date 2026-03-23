import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gitweb running')
@cli.command()
def start(): click.echo('gitweb started')
if __name__ == '__main__': cli()
