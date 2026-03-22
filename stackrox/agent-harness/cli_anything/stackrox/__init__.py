import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): click.echo('StackRox scan')
@cli.command()
def violations(): click.echo('StackRox violations')
if __name__ == '__main__': cli()
