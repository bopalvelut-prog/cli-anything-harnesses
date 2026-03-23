import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vessel running')
@cli.command()
def start(): click.echo('vessel started')
if __name__ == '__main__': cli()
