import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('course running')
@cli.command()
def start(): click.echo('course started')
if __name__ == '__main__': cli()
