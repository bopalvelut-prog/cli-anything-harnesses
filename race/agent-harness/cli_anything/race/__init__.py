import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('race running')
@cli.command()
def start(): click.echo('race started')
if __name__ == '__main__': cli()
