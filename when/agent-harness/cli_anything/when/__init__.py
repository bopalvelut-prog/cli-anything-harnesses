import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('when running')
@cli.command()
def start(): click.echo('when started')
if __name__ == '__main__': cli()
