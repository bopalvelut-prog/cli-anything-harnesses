import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('authentication running')
@cli.command()
def start(): click.echo('authentication started')
if __name__ == '__main__': cli()
