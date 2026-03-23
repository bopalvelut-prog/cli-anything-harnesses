import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('makefile running')
@cli.command()
def start(): click.echo('makefile started')
if __name__ == '__main__': cli()
