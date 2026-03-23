import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sentinel running')
@cli.command()
def start(): click.echo('sentinel started')
if __name__ == '__main__': cli()
