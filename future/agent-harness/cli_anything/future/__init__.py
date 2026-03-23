import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('future running')
@cli.command()
def start(): click.echo('future started')
if __name__ == '__main__': cli()
