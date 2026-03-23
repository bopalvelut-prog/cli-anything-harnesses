import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('face running')
@cli.command()
def start(): click.echo('face started')
if __name__ == '__main__': cli()
