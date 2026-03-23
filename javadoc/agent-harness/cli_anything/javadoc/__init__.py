import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('javadoc running')
@cli.command()
def start(): click.echo('javadoc started')
if __name__ == '__main__': cli()
