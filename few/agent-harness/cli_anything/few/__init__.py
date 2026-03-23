import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('few running')
@cli.command()
def start(): click.echo('few started')
if __name__ == '__main__': cli()
