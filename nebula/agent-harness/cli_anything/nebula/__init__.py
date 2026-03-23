import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nebula running')
@cli.command()
def start(): click.echo('nebula started')
if __name__ == '__main__': cli()
