import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('molecule running')
@cli.command()
def start(): click.echo('molecule started')
if __name__ == '__main__': cli()
