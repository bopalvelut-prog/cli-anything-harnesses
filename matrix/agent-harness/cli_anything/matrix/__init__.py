import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def rooms(): click.echo('Matrix rooms')
@cli.command()
def send(): click.echo('Matrix message')
if __name__ == '__main__': cli()
