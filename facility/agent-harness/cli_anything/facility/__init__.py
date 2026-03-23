import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('facility running')
@cli.command()
def start(): click.echo('facility started')
if __name__ == '__main__': cli()
