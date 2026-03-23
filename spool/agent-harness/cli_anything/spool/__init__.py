import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('spool running')
@cli.command()
def start(): click.echo('spool started')
if __name__ == '__main__': cli()
