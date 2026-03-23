import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('flink running')
@cli.command()
def start(): click.echo('flink started')
if __name__ == '__main__': cli()
