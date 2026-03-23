import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('backbone running')
@cli.command()
def start(): click.echo('backbone started')
if __name__ == '__main__': cli()
