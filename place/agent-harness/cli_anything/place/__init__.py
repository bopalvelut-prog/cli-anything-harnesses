import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('place running')
@cli.command()
def start(): click.echo('place started')
if __name__ == '__main__': cli()
