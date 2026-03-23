import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('solaris running')
@cli.command()
def start(): click.echo('solaris started')
if __name__ == '__main__': cli()
