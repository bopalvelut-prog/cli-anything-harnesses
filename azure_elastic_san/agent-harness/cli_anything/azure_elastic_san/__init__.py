import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_elastic_san running')
@cli.command()
def start(): click.echo('azure_elastic_san started')
if __name__ == '__main__': cli()
