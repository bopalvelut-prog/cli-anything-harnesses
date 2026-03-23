import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('boto running')
@cli.command()
def start(): click.echo('boto started')
if __name__ == '__main__': cli()
