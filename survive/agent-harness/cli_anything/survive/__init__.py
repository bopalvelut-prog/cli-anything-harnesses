import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('survive running')
@cli.command()
def start(): click.echo('survive started')
if __name__ == '__main__': cli()
