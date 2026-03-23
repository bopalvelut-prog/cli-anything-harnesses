import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grandmother running')
@cli.command()
def start(): click.echo('grandmother started')
if __name__ == '__main__': cli()
