import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('exact running')
@cli.command()
def start(): click.echo('exact started')
if __name__ == '__main__': cli()
