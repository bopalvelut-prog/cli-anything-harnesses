import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('favor running')
@cli.command()
def start(): click.echo('favor started')
if __name__ == '__main__': cli()
