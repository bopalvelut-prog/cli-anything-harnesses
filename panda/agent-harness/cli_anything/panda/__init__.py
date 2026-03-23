import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('panda running')
@cli.command()
def start(): click.echo('panda started')
if __name__ == '__main__': cli()
