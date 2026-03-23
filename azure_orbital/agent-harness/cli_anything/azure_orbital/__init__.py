import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_orbital running')
@cli.command()
def start(): click.echo('azure_orbital started')
if __name__ == '__main__': cli()
