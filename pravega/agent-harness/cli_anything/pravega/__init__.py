import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pravega running')
@cli.command()
def start(): click.echo('pravega started')
if __name__ == '__main__': cli()
