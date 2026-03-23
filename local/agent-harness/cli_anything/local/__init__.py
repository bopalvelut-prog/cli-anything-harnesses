import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('local running')
@cli.command()
def start(): click.echo('local started')
if __name__ == '__main__': cli()
