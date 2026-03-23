import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gcp_documentai running')
@cli.command()
def start(): click.echo('gcp_documentai started')
if __name__ == '__main__': cli()
