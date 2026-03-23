import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cdi running')
@cli.command()
def start(): click.echo('cdi started')
if __name__ == '__main__': cli()
