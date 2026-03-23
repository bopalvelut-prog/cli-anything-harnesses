import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gcp_bigtable running')
@cli.command()
def start(): click.echo('gcp_bigtable started')
if __name__ == '__main__': cli()
