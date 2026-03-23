import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('warehouse running')
@cli.command()
def start(): click.echo('warehouse started')
if __name__ == '__main__': cli()
