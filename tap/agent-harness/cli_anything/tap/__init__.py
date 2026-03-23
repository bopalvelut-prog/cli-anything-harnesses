import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tap running')
@cli.command()
def start(): click.echo('tap started')
if __name__ == '__main__': cli()
