import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('screenshot running')
@cli.command()
def start(): click.echo('screenshot started')
if __name__ == '__main__': cli()
