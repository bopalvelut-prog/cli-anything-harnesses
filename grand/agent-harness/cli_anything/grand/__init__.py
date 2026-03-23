import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grand running')
@cli.command()
def start(): click.echo('grand started')
if __name__ == '__main__': cli()
