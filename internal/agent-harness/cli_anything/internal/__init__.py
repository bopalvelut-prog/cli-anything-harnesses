import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('internal running')
@cli.command()
def start(): click.echo('internal started')
if __name__ == '__main__': cli()
