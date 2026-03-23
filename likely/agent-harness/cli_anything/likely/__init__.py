import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('likely running')
@cli.command()
def start(): click.echo('likely started')
if __name__ == '__main__': cli()
