import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ward running')
@cli.command()
def start(): click.echo('ward started')
if __name__ == '__main__': cli()
