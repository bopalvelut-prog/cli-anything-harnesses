import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('volcano running')
@cli.command()
def start(): click.echo('volcano started')
if __name__ == '__main__': cli()
