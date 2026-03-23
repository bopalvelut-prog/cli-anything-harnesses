import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dataproc running')
@cli.command()
def start(): click.echo('dataproc started')
if __name__ == '__main__': cli()
