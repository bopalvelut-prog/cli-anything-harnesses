import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('provision running')
@cli.command()
def start(): click.echo('provision started')
if __name__ == '__main__': cli()
