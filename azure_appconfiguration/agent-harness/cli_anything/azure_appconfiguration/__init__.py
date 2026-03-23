import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_appconfiguration running')
@cli.command()
def start(): click.echo('azure_appconfiguration started')
if __name__ == '__main__': cli()
