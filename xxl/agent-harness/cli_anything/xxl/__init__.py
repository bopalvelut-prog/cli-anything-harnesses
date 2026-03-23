import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xxl running')
@cli.command()
def start(): click.echo('xxl started')
if __name__ == '__main__': cli()
