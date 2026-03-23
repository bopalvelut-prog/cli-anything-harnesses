import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('degree running')
@cli.command()
def start(): click.echo('degree started')
if __name__ == '__main__': cli()
