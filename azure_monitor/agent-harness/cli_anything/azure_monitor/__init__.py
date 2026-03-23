import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_monitor running')
@cli.command()
def start(): click.echo('azure_monitor started')
if __name__ == '__main__': cli()
