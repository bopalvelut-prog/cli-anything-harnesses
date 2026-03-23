import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tang running')
@cli.command()
def start(): click.echo('tang started')
if __name__ == '__main__': cli()
