import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hunger running')
@cli.command()
def start(): click.echo('hunger started')
if __name__ == '__main__': cli()
