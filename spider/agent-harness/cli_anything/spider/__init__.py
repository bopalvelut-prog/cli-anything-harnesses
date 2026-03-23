import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('spider running')
@cli.command()
def start(): click.echo('spider started')
if __name__ == '__main__': cli()
