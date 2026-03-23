import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ship running')
@cli.command()
def start(): click.echo('ship started')
if __name__ == '__main__': cli()
