import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amalgam running')
@cli.command()
def start(): click.echo('amalgam started')
if __name__ == '__main__': cli()
