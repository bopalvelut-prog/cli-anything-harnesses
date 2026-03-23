import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('finalcut running')
@cli.command()
def start(): click.echo('finalcut started')
if __name__ == '__main__': cli()
