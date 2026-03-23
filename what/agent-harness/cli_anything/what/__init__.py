import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('what running')
@cli.command()
def start(): click.echo('what started')
if __name__ == '__main__': cli()
