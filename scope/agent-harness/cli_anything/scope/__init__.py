import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scope running')
@cli.command()
def start(): click.echo('scope started')
if __name__ == '__main__': cli()
