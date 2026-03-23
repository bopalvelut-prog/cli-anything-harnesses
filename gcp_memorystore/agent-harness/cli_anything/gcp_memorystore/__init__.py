import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gcp_memorystore running')
@cli.command()
def start(): click.echo('gcp_memorystore started')
if __name__ == '__main__': cli()
