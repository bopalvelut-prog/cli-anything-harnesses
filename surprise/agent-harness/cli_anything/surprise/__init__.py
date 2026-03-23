import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('surprise running')
@cli.command()
def start(): click.echo('surprise started')
if __name__ == '__main__': cli()
