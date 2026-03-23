import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('docker_compose running')
@cli.command()
def start(): click.echo('docker_compose started')
if __name__ == '__main__': cli()
