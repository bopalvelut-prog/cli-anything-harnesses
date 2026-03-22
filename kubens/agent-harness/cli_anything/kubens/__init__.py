import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def switch(): subprocess.run(['kubens'])
@cli.command()
def current(): click.echo('Current namespace')
if __name__ == '__main__': cli()
