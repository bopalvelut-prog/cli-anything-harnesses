import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_digitaltwins running')
@cli.command()
def start(): click.echo('azure_digitaltwins started')
if __name__ == '__main__': cli()
