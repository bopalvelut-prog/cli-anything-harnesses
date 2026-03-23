import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('astral running')
@cli.command()
def start(): click.echo('astral started')
if __name__ == '__main__': cli()
