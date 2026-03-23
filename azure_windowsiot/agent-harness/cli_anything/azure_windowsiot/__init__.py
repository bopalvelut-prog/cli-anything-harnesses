import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_windowsiot running')
@cli.command()
def start(): click.echo('azure_windowsiot started')
if __name__ == '__main__': cli()
