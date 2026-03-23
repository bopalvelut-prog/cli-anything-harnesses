import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('json running')
@cli.command()
def start(): click.echo('json started')
if __name__ == '__main__': cli()
