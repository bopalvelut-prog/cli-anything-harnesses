import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nnode running')
@cli.command()
def start(): click.echo('nnode started')
if __name__ == '__main__': cli()
