import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('firefly running')
@cli.command()
def start(): click.echo('firefly started')
if __name__ == '__main__': cli()
