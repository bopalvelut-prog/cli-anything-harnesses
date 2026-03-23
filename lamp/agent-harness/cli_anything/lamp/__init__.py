import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lamp running')
@cli.command()
def start(): click.echo('lamp started')
if __name__ == '__main__': cli()
