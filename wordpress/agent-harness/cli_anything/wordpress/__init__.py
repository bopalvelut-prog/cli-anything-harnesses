import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def install(): click.echo('WordPress installed')
@cli.command()
def plugins(): click.echo('WordPress plugins')
if __name__ == '__main__': cli()
