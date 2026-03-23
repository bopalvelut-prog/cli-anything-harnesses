import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('film running')
@cli.command()
def start(): click.echo('film started')
if __name__ == '__main__': cli()
