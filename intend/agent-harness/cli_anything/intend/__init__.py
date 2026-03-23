import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('intend running')
@cli.command()
def start(): click.echo('intend started')
if __name__ == '__main__': cli()
