import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_sentinel running')
@cli.command()
def start(): click.echo('azure_sentinel started')
if __name__ == '__main__': cli()
