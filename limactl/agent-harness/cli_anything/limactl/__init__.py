import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('limactl running')
@cli.command()
def start(): click.echo('limactl started')
if __name__ == '__main__': cli()
