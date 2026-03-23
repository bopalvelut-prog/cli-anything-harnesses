import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_billing running')
@cli.command()
def start(): click.echo('azure_billing started')
if __name__ == '__main__': cli()
