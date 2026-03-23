import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('slow running')
@cli.command()
def start(): click.echo('slow started')
if __name__ == '__main__': cli()
