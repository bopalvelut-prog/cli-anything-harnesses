import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('partitions running')
@cli.command()
def start(): click.echo('partitions started')
if __name__ == '__main__': cli()
