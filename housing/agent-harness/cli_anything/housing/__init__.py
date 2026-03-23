import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('housing running')
@cli.command()
def start(): click.echo('housing started')
if __name__ == '__main__': cli()
