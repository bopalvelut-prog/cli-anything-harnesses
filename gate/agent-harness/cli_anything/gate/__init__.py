import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gate running')
@cli.command()
def start(): click.echo('gate started')
if __name__ == '__main__': cli()
