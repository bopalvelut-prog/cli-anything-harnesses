import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tent running')
@cli.command()
def start(): click.echo('tent started')
if __name__ == '__main__': cli()
