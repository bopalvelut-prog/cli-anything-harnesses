import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wallet running')
@cli.command()
def start(): click.echo('wallet started')
if __name__ == '__main__': cli()
