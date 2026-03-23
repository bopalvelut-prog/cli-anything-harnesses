import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('eventually running')
@cli.command()
def start(): click.echo('eventually started')
if __name__ == '__main__': cli()
