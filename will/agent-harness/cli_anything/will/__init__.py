import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('will running')
@cli.command()
def start(): click.echo('will started')
if __name__ == '__main__': cli()
