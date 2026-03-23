import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('oauth running')
@cli.command()
def start(): click.echo('oauth started')
if __name__ == '__main__': cli()
