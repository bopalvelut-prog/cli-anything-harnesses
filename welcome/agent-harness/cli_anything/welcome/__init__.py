import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('welcome running')
@cli.command()
def start(): click.echo('welcome started')
if __name__ == '__main__': cli()
