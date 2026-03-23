import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xml running')
@cli.command()
def start(): click.echo('xml started')
if __name__ == '__main__': cli()
