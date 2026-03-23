import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('k8s running')
@cli.command()
def start(): click.echo('k8s started')
if __name__ == '__main__': cli()
