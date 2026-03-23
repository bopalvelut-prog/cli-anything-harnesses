import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('necessarily running')
@cli.command()
def start(): click.echo('necessarily started')
if __name__ == '__main__': cli()
