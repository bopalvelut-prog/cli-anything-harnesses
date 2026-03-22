import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('OpenProject running')
@cli.command()
def projects(): click.echo('OpenProject projects')
if __name__ == '__main__': cli()
