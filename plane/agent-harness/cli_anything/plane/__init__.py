import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Plane started')
@cli.command()
def projects(): click.echo('Plane projects')
if __name__ == '__main__': cli()
