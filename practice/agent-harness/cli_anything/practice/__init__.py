import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('practice running')
@cli.command()
def start(): click.echo('practice started')
if __name__ == '__main__': cli()
