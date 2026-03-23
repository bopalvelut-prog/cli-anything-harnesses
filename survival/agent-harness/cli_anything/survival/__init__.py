import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('survival running')
@cli.command()
def start(): click.echo('survival started')
if __name__ == '__main__': cli()
