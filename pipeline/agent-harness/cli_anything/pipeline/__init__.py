import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pipeline running')
@cli.command()
def start(): click.echo('pipeline started')
if __name__ == '__main__': cli()
