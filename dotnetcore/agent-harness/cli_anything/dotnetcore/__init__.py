import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dotnetcore running')
@cli.command()
def start(): click.echo('dotnetcore started')
if __name__ == '__main__': cli()
