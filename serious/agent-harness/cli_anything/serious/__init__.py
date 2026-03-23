import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('serious running')
@cli.command()
def start(): click.echo('serious started')
if __name__ == '__main__': cli()
