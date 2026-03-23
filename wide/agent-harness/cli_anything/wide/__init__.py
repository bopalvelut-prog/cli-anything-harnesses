import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wide running')
@cli.command()
def start(): click.echo('wide started')
if __name__ == '__main__': cli()
