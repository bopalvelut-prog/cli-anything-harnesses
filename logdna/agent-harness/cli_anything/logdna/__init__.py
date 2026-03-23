import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('logdna running')
@cli.command()
def start(): click.echo('logdna started')
if __name__ == '__main__': cli()
