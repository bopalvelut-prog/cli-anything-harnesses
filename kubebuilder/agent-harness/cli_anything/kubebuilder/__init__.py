import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kubebuilder running')
@cli.command()
def start(): click.echo('kubebuilder started')
if __name__ == '__main__': cli()
