import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('royal running')
@cli.command()
def start(): click.echo('royal started')
if __name__ == '__main__': cli()
