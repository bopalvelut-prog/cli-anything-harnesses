import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def open(): click.echo('draw.io opened')
@cli.command()
def export(): click.echo('Export diagram')
if __name__ == '__main__': cli()
