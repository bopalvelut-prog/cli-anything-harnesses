import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_communication running')
@cli.command()
def start(): click.echo('azure_communication started')
if __name__ == '__main__': cli()
