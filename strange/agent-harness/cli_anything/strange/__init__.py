import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('strange running')
@cli.command()
def start(): click.echo('strange started')
if __name__ == '__main__': cli()
