import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nvm running')
@cli.command()
def start(): click.echo('nvm started')
if __name__ == '__main__': cli()
