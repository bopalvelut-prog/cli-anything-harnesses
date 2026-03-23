import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('detect running')
@cli.command()
def start(): click.echo('detect started')
if __name__ == '__main__': cli()
