import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rspec running')
@cli.command()
def start(): click.echo('rspec started')
if __name__ == '__main__': cli()
