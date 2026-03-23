import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('flannel running')
@cli.command()
def start(): click.echo('flannel started')
if __name__ == '__main__': cli()
