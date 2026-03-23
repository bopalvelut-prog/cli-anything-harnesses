import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gui running')
@cli.command()
def start(): click.echo('gui started')
if __name__ == '__main__': cli()
