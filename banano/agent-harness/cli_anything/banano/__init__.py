import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def wallet(): click.echo('Banano wallet')
if __name__ == '__main__': cli()
