import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('writing running')
@cli.command()
def start(): click.echo('writing started')
if __name__ == '__main__': cli()
