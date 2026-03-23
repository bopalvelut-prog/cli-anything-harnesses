import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('retain running')
@cli.command()
def start(): click.echo('retain started')
if __name__ == '__main__': cli()
