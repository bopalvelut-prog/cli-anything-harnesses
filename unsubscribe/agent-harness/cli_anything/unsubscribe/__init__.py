import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unsubscribe running')
@cli.command()
def start(): click.echo('unsubscribe started')
if __name__ == '__main__': cli()
