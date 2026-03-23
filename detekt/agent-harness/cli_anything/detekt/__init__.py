import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('detekt running')
@cli.command()
def start(): click.echo('detekt started')
if __name__ == '__main__': cli()
