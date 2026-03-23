import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_confidentialledger running')
@cli.command()
def start(): click.echo('azure_confidentialledger started')
if __name__ == '__main__': cli()
