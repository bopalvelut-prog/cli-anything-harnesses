import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pipe running')
@cli.command()
def start(): click.echo('pipe started')
if __name__ == '__main__': cli()
