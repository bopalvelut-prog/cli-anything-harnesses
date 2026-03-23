import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('career running')
@cli.command()
def start(): click.echo('career started')
if __name__ == '__main__': cli()
