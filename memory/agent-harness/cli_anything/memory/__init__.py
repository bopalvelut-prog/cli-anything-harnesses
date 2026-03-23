import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('memory running')
@cli.command()
def start(): click.echo('memory started')
if __name__ == '__main__': cli()
