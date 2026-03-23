import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stem running')
@cli.command()
def start(): click.echo('stem started')
if __name__ == '__main__': cli()
