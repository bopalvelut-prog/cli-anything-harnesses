import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_powerbiembedded running')
@cli.command()
def start(): click.echo('azure_powerbiembedded started')
if __name__ == '__main__': cli()
