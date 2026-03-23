import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('exercism running')
@cli.command()
def start(): click.echo('exercism started')
if __name__ == '__main__': cli()
