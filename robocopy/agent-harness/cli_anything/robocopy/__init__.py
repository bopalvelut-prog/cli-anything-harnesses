import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('source')
@click.argument('dest')
def copy(source, dest): click.echo(f'Robocopy: {source} -> {dest}')
if __name__ == '__main__': cli()
