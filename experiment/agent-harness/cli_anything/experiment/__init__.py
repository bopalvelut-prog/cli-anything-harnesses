import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('experiment running')
@cli.command()
def start(): click.echo('experiment started')
if __name__ == '__main__': cli()
