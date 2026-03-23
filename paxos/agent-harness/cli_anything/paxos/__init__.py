import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('paxos running')
@cli.command()
def start(): click.echo('paxos started')
if __name__ == '__main__': cli()
