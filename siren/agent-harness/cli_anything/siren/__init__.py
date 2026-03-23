import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('siren running')
@cli.command()
def start(): click.echo('siren started')
if __name__ == '__main__': cli()
