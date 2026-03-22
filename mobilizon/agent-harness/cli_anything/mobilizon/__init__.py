import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def events(): click.echo('Mobilizon events')
@cli.command()
def groups(): click.echo('Mobilizon groups')
if __name__ == '__main__': cli()
