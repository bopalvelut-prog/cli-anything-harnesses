import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reporter running')
@cli.command()
def start(): click.echo('reporter started')
if __name__ == '__main__': cli()
