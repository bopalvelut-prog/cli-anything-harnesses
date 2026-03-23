import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('retries running')
@cli.command()
def start(): click.echo('retries started')
if __name__ == '__main__': cli()
