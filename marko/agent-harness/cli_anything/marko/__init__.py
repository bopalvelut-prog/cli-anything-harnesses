import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('marko running')
@cli.command()
def start(): click.echo('marko started')
if __name__ == '__main__': cli()
