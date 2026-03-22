import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def switch(): subprocess.run(['kubectx'])
@cli.command()
def current(): click.echo('Current context')
if __name__ == '__main__': cli()
