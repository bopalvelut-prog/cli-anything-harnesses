import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_kubernetes running')
@cli.command()
def start(): click.echo('azure_kubernetes started')
if __name__ == '__main__': cli()
