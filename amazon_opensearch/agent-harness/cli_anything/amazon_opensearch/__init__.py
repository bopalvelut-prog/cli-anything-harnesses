import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amazon_opensearch running')
@cli.command()
def start(): click.echo('amazon_opensearch started')
if __name__ == '__main__': cli()
