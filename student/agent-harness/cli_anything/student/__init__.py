import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('student running')
@cli.command()
def start(): click.echo('student started')
if __name__ == '__main__': cli()
