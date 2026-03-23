import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pdf running')
@cli.command()
def start(): click.echo('pdf started')
if __name__ == '__main__': cli()
