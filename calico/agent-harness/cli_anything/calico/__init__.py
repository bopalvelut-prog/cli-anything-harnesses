import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('calico running')
@cli.command()
def start(): click.echo('calico started')
if __name__ == '__main__': cli()
