import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('previous running')
@cli.command()
def start(): click.echo('previous started')
if __name__ == '__main__': cli()
