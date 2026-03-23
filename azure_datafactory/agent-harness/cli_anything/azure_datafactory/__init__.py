import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_datafactory running')
@cli.command()
def start(): click.echo('azure_datafactory started')
if __name__ == '__main__': cli()
