import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('banana running')
@cli.command()
def start(): click.echo('banana started')
if __name__ == '__main__': cli()
