import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def wallet(): click.echo('Ravencoin wallet')
if __name__ == '__main__': cli()
