import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jsonld running')
@cli.command()
def start(): click.echo('jsonld started')
if __name__ == '__main__': cli()
