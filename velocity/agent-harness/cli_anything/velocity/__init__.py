import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('velocity running')
@cli.command()
def start(): click.echo('velocity started')
if __name__ == '__main__': cli()
