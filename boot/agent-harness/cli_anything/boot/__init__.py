import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('boot running')
@cli.command()
def start(): click.echo('boot started')
if __name__ == '__main__': cli()
