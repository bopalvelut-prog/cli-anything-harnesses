import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('arnold running')
@cli.command()
def start(): click.echo('arnold started')
if __name__ == '__main__': cli()
