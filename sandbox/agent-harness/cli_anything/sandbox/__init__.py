import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sandbox running')
@cli.command()
def start(): click.echo('sandbox started')
if __name__ == '__main__': cli()
