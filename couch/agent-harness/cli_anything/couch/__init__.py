import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('couch running')
@cli.command()
def start(): click.echo('couch started')
if __name__ == '__main__': cli()
