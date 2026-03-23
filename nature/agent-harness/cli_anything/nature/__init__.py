import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nature running')
@cli.command()
def start(): click.echo('nature started')
if __name__ == '__main__': cli()
