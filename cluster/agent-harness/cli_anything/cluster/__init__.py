import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cluster running')
@cli.command()
def start(): click.echo('cluster started')
if __name__ == '__main__': cli()
