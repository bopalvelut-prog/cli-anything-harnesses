import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('angr running')
@cli.command()
def start(): click.echo('angr started')
if __name__ == '__main__': cli()
