import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('retl running')
@cli.command()
def start(): click.echo('retl started')
if __name__ == '__main__': cli()
