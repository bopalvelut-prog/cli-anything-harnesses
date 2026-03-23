import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('variant running')
@cli.command()
def start(): click.echo('variant started')
if __name__ == '__main__': cli()
