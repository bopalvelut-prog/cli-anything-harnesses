import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('osquery running')
@cli.command()
def start(): click.echo('osquery started')
if __name__ == '__main__': cli()
