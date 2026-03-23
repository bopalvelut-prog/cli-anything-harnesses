import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('clock running')
@cli.command()
def start(): click.echo('clock started')
if __name__ == '__main__': cli()
