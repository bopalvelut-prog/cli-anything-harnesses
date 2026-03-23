import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('death running')
@cli.command()
def start(): click.echo('death started')
if __name__ == '__main__': cli()
