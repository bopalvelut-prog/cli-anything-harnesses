import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('org running')
@cli.command()
def start(): click.echo('org started')
if __name__ == '__main__': cli()
