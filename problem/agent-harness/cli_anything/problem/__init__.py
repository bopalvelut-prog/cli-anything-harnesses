import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('problem running')
@cli.command()
def start(): click.echo('problem started')
if __name__ == '__main__': cli()
