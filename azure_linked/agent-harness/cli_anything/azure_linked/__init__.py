import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_linked running')
@cli.command()
def start(): click.echo('azure_linked started')
if __name__ == '__main__': cli()
