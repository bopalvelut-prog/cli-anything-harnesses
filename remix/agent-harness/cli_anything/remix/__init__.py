import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def open(): click.echo('Remix IDE opened')
if __name__ == '__main__': cli()
