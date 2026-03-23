import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bus running')
@cli.command()
def start(): click.echo('bus started')
if __name__ == '__main__': cli()
