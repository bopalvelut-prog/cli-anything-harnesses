import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('leave running')
@cli.command()
def start(): click.echo('leave started')
if __name__ == '__main__': cli()
