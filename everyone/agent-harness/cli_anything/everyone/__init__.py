import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('everyone running')
@cli.command()
def start(): click.echo('everyone started')
if __name__ == '__main__': cli()
