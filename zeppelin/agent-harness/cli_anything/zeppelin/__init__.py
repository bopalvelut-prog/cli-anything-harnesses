import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('zeppelin running')
@cli.command()
def start(): click.echo('zeppelin started')
if __name__ == '__main__': cli()
