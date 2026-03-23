import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('marlin running')
@cli.command()
def start(): click.echo('marlin started')
if __name__ == '__main__': cli()
