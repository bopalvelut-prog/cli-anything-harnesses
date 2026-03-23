import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('virtue running')
@cli.command()
def start(): click.echo('virtue started')
if __name__ == '__main__': cli()
