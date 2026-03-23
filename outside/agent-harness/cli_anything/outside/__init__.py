import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('outside running')
@cli.command()
def start(): click.echo('outside started')
if __name__ == '__main__': cli()
