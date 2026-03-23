import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aria running')
@cli.command()
def start(): click.echo('aria started')
if __name__ == '__main__': cli()
