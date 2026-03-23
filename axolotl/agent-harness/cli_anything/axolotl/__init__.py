import click
@click.group()
def cli(): pass
@cli.command()
def train(): click.echo('Axolotl train')
@cli.command()
def config(): click.echo('Axolotl config')
if __name__ == '__main__': cli()
