import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ppa running')
@cli.command()
def start(): click.echo('ppa started')
if __name__ == '__main__': cli()
