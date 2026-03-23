import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tree running')
@cli.command()
def start(): click.echo('tree started')
if __name__ == '__main__': cli()
