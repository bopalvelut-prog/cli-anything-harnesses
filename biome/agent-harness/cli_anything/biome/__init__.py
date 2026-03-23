import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('biome running')
@cli.command()
def start(): click.echo('biome started')
if __name__ == '__main__': cli()
