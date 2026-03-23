import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('restrict running')
@cli.command()
def start(): click.echo('restrict started')
if __name__ == '__main__': cli()
