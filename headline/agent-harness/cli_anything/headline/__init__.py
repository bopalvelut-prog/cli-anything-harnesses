import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('headline running')
@cli.command()
def start(): click.echo('headline started')
if __name__ == '__main__': cli()
