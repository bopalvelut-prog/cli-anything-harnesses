import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tomato running')
@cli.command()
def start(): click.echo('tomato started')
if __name__ == '__main__': cli()
