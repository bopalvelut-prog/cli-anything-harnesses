import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('keygen running')
@cli.command()
def start(): click.echo('keygen started')
if __name__ == '__main__': cli()
