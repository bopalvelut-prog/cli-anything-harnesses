import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cni running')
@cli.command()
def start(): click.echo('cni started')
if __name__ == '__main__': cli()
