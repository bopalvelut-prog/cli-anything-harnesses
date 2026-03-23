import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('oracle running')
@cli.command()
def start(): click.echo('oracle started')
if __name__ == '__main__': cli()
