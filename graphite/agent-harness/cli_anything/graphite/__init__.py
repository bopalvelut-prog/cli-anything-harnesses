import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('graphite running')
@cli.command()
def start(): click.echo('graphite started')
if __name__ == '__main__': cli()
