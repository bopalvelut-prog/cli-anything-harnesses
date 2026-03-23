import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('server running')
@cli.command()
def start(): click.echo('server started')
if __name__ == '__main__': cli()
