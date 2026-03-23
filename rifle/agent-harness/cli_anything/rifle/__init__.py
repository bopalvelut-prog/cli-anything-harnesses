import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rifle running')
@cli.command()
def start(): click.echo('rifle started')
if __name__ == '__main__': cli()
