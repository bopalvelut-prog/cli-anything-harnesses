import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('google_docs running')
@cli.command()
def start(): click.echo('google_docs started')
if __name__ == '__main__': cli()
