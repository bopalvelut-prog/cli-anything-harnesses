import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def post(): click.echo('Pixelfed post')
@cli.command()
def feed(): click.echo('Pixelfed feed')
if __name__ == '__main__': cli()
