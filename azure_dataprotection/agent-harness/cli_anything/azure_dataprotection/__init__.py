import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_dataprotection running')
@cli.command()
def start(): click.echo('azure_dataprotection started')
if __name__ == '__main__': cli()
