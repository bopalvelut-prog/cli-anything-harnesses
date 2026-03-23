import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('support running')
@cli.command()
def start(): click.echo('support started')
if __name__ == '__main__': cli()
