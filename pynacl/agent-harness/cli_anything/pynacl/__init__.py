import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pynacl running')
@cli.command()
def start(): click.echo('pynacl started')
if __name__ == '__main__': cli()
