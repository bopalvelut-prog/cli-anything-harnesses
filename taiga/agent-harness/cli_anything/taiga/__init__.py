import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Taiga started')
@cli.command()
def projects(): click.echo('Taiga projects')
if __name__ == '__main__': cli()
