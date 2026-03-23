import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('typography running')
@cli.command()
def start(): click.echo('typography started')
if __name__ == '__main__': cli()
