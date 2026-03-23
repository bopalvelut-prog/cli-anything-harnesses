import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('suppose running')
@cli.command()
def start(): click.echo('suppose started')
if __name__ == '__main__': cli()
