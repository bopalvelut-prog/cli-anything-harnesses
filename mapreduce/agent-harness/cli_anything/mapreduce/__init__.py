import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mapreduce running')
@cli.command()
def start(): click.echo('mapreduce started')
if __name__ == '__main__': cli()
