import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('salary running')
@cli.command()
def start(): click.echo('salary started')
if __name__ == '__main__': cli()
