import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('purity running')
@cli.command()
def start(): click.echo('purity started')
if __name__ == '__main__': cli()
