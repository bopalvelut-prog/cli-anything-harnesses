import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('luci running')
@cli.command()
def start(): click.echo('luci started')
if __name__ == '__main__': cli()
