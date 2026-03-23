import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lion running')
@cli.command()
def start(): click.echo('lion started')
if __name__ == '__main__': cli()
