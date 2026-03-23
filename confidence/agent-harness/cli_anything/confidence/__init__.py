import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('confidence running')
@cli.command()
def start(): click.echo('confidence started')
if __name__ == '__main__': cli()
