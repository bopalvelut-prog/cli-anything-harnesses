import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_avalanche running')
@cli.command()
def start(): click.echo('azure_avalanche started')
if __name__ == '__main__': cli()
