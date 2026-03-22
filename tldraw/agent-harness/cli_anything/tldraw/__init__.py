import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def open(): click.echo('tldraw opened')
@cli.command()
def export(): click.echo('Export canvas')
if __name__ == '__main__': cli()
