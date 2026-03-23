import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('plaid running')
@cli.command()
def start(): click.echo('plaid started')
if __name__ == '__main__': cli()
