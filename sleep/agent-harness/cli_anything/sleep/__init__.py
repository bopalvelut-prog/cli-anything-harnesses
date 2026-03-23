import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sleep running')
@cli.command()
def start(): click.echo('sleep started')
if __name__ == '__main__': cli()
