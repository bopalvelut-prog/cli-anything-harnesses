import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('passage running')
@cli.command()
def start(): click.echo('passage started')
if __name__ == '__main__': cli()
