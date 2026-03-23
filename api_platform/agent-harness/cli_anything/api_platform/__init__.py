import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('api_platform running')
@cli.command()
def start(): click.echo('api_platform started')
if __name__ == '__main__': cli()
