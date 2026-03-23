import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('which running')
@cli.command()
def start(): click.echo('which started')
if __name__ == '__main__': cli()
