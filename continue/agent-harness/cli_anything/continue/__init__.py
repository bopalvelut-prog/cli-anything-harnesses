import click
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Continue start')
@cli.command()
def config(): click.echo('Continue config')
if __name__ == '__main__': cli()
