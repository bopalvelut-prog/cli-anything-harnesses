import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kruise running')
@cli.command()
def start(): click.echo('kruise started')
if __name__ == '__main__': cli()
