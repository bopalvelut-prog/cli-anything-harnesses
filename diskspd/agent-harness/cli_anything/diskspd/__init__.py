import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('diskspd running')
@cli.command()
def start(): click.echo('diskspd started')
if __name__ == '__main__': cli()
