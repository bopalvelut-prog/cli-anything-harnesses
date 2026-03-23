import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('service running')
@cli.command()
def start(): click.echo('service started')
if __name__ == '__main__': cli()
