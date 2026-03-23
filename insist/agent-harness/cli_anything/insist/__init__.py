import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('insist running')
@cli.command()
def start(): click.echo('insist started')
if __name__ == '__main__': cli()
