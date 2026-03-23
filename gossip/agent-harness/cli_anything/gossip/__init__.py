import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gossip running')
@cli.command()
def start(): click.echo('gossip started')
if __name__ == '__main__': cli()
