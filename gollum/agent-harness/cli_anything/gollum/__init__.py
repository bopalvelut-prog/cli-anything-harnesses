import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gollum running')
@cli.command()
def start(): click.echo('gollum started')
if __name__ == '__main__': cli()
