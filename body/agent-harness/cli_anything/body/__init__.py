import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('body running')
@cli.command()
def start(): click.echo('body started')
if __name__ == '__main__': cli()
