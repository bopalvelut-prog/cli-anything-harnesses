import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('color running')
@cli.command()
def start(): click.echo('color started')
if __name__ == '__main__': cli()
