import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lightbend running')
@cli.command()
def start(): click.echo('lightbend started')
if __name__ == '__main__': cli()
