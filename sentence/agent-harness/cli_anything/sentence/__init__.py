import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sentence running')
@cli.command()
def start(): click.echo('sentence started')
if __name__ == '__main__': cli()
