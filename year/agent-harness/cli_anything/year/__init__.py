import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('year running')
@cli.command()
def start(): click.echo('year started')
if __name__ == '__main__': cli()
