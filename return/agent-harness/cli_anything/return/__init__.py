import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('return running')
@cli.command()
def start(): click.echo('return started')
if __name__ == '__main__': cli()
