import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Seafile running')
@cli.command()
def libraries(): click.echo('Seafile libraries')
if __name__ == '__main__': cli()
