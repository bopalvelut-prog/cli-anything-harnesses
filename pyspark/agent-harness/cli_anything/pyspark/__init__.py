import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pyspark running')
@cli.command()
def start(): click.echo('pyspark started')
if __name__ == '__main__': cli()
