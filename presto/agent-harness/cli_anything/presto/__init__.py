import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('presto running')
@cli.command()
def start(): click.echo('presto started')
if __name__ == '__main__': cli()
