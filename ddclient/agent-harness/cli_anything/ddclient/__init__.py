import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ddclient running')
@cli.command()
def start(): click.echo('ddclient started')
if __name__ == '__main__': cli()
