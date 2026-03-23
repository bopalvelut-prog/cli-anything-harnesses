import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hunt running')
@cli.command()
def start(): click.echo('hunt started')
if __name__ == '__main__': cli()
