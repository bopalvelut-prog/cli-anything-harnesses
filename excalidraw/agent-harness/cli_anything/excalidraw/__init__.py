import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def open(): click.echo('Excalidraw opened')
@cli.command()
def export(): click.echo('Export drawing')
if __name__ == '__main__': cli()
