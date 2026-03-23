import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('alloy running')
@cli.command()
def start(): click.echo('alloy started')
if __name__ == '__main__': cli()
