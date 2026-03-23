import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('trap running')
@cli.command()
def start(): click.echo('trap started')
if __name__ == '__main__': cli()
