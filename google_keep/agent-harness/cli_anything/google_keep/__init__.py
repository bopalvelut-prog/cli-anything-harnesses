import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('google_keep running')
@cli.command()
def start(): click.echo('google_keep started')
if __name__ == '__main__': cli()
