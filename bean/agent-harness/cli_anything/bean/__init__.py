import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bean running')
@cli.command()
def start(): click.echo('bean started')
if __name__ == '__main__': cli()
