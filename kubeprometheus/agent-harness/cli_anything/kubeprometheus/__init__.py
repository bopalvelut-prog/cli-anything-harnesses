import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kubeprometheus running')
@cli.command()
def start(): click.echo('kubeprometheus started')
if __name__ == '__main__': cli()
