import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sink running')
@cli.command()
def start(): click.echo('sink started')
if __name__ == '__main__': cli()
