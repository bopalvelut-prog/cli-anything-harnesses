import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ultra running')
@cli.command()
def start(): click.echo('ultra started')
if __name__ == '__main__': cli()
