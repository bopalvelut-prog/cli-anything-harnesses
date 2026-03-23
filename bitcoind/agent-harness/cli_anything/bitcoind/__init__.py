import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bitcoind running')
@cli.command()
def start(): click.echo('bitcoind started')
if __name__ == '__main__': cli()
