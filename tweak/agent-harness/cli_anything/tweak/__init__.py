import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tweak running')
@cli.command()
def start(): click.echo('tweak started')
if __name__ == '__main__': cli()
