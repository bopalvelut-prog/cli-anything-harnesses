import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('loud running')
@cli.command()
def start(): click.echo('loud started')
if __name__ == '__main__': cli()
