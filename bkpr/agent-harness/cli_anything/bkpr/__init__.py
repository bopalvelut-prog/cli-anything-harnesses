import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bkpr running')
@cli.command()
def start(): click.echo('bkpr started')
if __name__ == '__main__': cli()
