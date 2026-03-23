import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nail running')
@cli.command()
def start(): click.echo('nail started')
if __name__ == '__main__': cli()
