import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amber running')
@cli.command()
def start(): click.echo('amber started')
if __name__ == '__main__': cli()
