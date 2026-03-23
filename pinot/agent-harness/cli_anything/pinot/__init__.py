import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pinot running')
@cli.command()
def start(): click.echo('pinot started')
if __name__ == '__main__': cli()
