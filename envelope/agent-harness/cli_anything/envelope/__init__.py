import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('envelope running')
@cli.command()
def start(): click.echo('envelope started')
if __name__ == '__main__': cli()
