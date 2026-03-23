import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fault running')
@cli.command()
def start(): click.echo('fault started')
if __name__ == '__main__': cli()
