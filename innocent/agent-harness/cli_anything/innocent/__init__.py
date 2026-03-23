import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('innocent running')
@cli.command()
def start(): click.echo('innocent started')
if __name__ == '__main__': cli()
