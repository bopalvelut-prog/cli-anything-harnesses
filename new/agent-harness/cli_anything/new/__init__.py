import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('new running')
@cli.command()
def start(): click.echo('new started')
if __name__ == '__main__': cli()
