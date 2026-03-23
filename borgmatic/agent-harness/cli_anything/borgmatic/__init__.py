import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('borgmatic running')
@cli.command()
def start(): click.echo('borgmatic started')
if __name__ == '__main__': cli()
