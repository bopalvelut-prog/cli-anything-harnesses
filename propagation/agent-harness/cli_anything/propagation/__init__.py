import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('propagation running')
@cli.command()
def start(): click.echo('propagation started')
if __name__ == '__main__': cli()
