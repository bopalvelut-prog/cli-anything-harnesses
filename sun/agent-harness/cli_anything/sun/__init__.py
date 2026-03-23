import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sun running')
@cli.command()
def start(): click.echo('sun started')
if __name__ == '__main__': cli()
