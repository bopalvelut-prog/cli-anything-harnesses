import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('davmail running')
@cli.command()
def start(): click.echo('davmail started')
if __name__ == '__main__': cli()
