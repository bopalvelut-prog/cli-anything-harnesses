import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('arc running')
@cli.command()
def start(): click.echo('arc started')
if __name__ == '__main__': cli()
