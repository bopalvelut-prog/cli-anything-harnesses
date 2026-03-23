import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('worth running')
@cli.command()
def start(): click.echo('worth started')
if __name__ == '__main__': cli()
