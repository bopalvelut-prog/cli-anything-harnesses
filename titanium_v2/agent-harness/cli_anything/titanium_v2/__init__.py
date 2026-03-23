import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('titanium_v2 running')
@cli.command()
def start(): click.echo('titanium_v2 started')
if __name__ == '__main__': cli()
