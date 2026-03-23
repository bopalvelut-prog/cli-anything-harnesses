import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_devtestlabs running')
@cli.command()
def start(): click.echo('azure_devtestlabs started')
if __name__ == '__main__': cli()
