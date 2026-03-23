import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ssl running')
@cli.command()
def start(): click.echo('ssl started')
if __name__ == '__main__': cli()
