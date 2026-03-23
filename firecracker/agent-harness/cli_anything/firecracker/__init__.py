import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('firecracker running')
@cli.command()
def start(): click.echo('firecracker started')
if __name__ == '__main__': cli()
