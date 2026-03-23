import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('redpanda running')
@cli.command()
def start(): click.echo('redpanda started')
if __name__ == '__main__': cli()
