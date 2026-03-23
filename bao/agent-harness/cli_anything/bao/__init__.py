import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bao running')
@cli.command()
def start(): click.echo('bao started')
if __name__ == '__main__': cli()
