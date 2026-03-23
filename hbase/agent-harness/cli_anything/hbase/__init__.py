import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hbase running')
@cli.command()
def start(): click.echo('hbase started')
if __name__ == '__main__': cli()
