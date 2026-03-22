import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('IFTTT applets')
@cli.command()
def run(): click.echo('IFTTT run')
if __name__ == '__main__': cli()
