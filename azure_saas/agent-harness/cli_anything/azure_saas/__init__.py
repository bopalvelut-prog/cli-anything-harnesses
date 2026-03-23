import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_saas running')
@cli.command()
def start(): click.echo('azure_saas started')
if __name__ == '__main__': cli()
