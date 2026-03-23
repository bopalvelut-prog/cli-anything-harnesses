import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kubelet running')
@cli.command()
def start(): click.echo('kubelet started')
if __name__ == '__main__': cli()
