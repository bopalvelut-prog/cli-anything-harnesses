import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('criminal running')
@cli.command()
def start(): click.echo('criminal started')
if __name__ == '__main__': cli()
