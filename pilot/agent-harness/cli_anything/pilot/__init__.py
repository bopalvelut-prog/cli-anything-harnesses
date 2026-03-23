import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pilot running')
@cli.command()
def start(): click.echo('pilot started')
if __name__ == '__main__': cli()
