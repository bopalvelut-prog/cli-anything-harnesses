import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lecture running')
@cli.command()
def start(): click.echo('lecture started')
if __name__ == '__main__': cli()
