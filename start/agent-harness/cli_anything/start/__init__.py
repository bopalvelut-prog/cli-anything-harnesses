import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('start running')
@cli.command()
def start(): click.echo('start started')
if __name__ == '__main__': cli()
