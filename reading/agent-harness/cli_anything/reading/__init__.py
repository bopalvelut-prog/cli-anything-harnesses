import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reading running')
@cli.command()
def start(): click.echo('reading started')
if __name__ == '__main__': cli()
