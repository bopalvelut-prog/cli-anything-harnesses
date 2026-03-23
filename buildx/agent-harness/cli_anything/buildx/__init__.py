import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('buildx running')
@cli.command()
def start(): click.echo('buildx started')
if __name__ == '__main__': cli()
