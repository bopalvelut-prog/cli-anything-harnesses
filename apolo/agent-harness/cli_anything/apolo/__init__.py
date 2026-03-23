import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apolo running')
@cli.command()
def start(): click.echo('apolo started')
if __name__ == '__main__': cli()
