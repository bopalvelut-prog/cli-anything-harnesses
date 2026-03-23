import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('proposal running')
@cli.command()
def start(): click.echo('proposal started')
if __name__ == '__main__': cli()
