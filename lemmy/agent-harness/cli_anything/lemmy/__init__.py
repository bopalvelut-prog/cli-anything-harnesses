import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def post(): click.echo('Lemmy post')
@cli.command()
def feed(): click.echo('Lemmy feed')
if __name__ == '__main__': cli()
