import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('organic running')
@cli.command()
def start(): click.echo('organic started')
if __name__ == '__main__': cli()
