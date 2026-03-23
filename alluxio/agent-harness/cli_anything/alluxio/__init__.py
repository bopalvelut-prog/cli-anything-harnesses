import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('alluxio running')
@cli.command()
def start(): click.echo('alluxio started')
if __name__ == '__main__': cli()
