import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('file running')
@cli.command()
def start(): click.echo('file started')
if __name__ == '__main__': cli()
