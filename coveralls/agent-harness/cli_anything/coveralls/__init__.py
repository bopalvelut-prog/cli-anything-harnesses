import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('coveralls running')
@cli.command()
def start(): click.echo('coveralls started')
if __name__ == '__main__': cli()
