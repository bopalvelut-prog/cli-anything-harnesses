import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('datapipeline running')
@cli.command()
def start(): click.echo('datapipeline started')
if __name__ == '__main__': cli()
