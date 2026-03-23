import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prod running')
@cli.command()
def start(): click.echo('prod started')
if __name__ == '__main__': cli()
