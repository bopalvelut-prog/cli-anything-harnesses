import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('defold running')
@cli.command()
def start(): click.echo('defold started')
if __name__ == '__main__': cli()
