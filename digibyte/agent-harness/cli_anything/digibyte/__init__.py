import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('DigiByte node')
@cli.command()
def wallet(): click.echo('DigiByte wallet')
if __name__ == '__main__': cli()
