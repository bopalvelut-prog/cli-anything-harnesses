import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unusual running')
@cli.command()
def start(): click.echo('unusual started')
if __name__ == '__main__': cli()
