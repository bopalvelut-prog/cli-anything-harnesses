import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Collabora running')
@cli.command()
def docs(): click.echo('Collabora docs')
if __name__ == '__main__': cli()
