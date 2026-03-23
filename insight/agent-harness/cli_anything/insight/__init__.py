import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('insight running')
@cli.command()
def start(): click.echo('insight started')
if __name__ == '__main__': cli()
