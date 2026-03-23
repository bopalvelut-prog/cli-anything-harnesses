import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nearly running')
@cli.command()
def start(): click.echo('nearly started')
if __name__ == '__main__': cli()
