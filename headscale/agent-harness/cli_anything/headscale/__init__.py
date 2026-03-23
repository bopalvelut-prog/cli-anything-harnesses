import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('headscale running')
@cli.command()
def start(): click.echo('headscale started')
if __name__ == '__main__': cli()
