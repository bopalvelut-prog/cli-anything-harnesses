import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mayor running')
@cli.command()
def start(): click.echo('mayor started')
if __name__ == '__main__': cli()
