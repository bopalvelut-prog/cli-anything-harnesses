import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gcp_dataproc running')
@cli.command()
def start(): click.echo('gcp_dataproc started')
if __name__ == '__main__': cli()
