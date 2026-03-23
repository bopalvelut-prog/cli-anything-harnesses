import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('inquiry running')
@cli.command()
def start(): click.echo('inquiry started')
if __name__ == '__main__': cli()
