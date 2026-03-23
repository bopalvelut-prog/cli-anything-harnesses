import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('whom running')
@cli.command()
def start(): click.echo('whom started')
if __name__ == '__main__': cli()
