import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pocket running')
@cli.command()
def start(): click.echo('pocket started')
if __name__ == '__main__': cli()
