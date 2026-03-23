import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cap running')
@cli.command()
def start(): click.echo('cap started')
if __name__ == '__main__': cli()
