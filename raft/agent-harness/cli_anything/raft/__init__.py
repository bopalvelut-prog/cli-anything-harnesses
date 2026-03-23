import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('raft running')
@cli.command()
def start(): click.echo('raft started')
if __name__ == '__main__': cli()
