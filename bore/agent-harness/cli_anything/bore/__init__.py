import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bore running')
@cli.command()
def start(): click.echo('bore started')
if __name__ == '__main__': cli()
