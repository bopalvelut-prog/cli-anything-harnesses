import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fall running')
@cli.command()
def start(): click.echo('fall started')
if __name__ == '__main__': cli()
