import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ondatra running')
@cli.command()
def start(): click.echo('ondatra started')
if __name__ == '__main__': cli()
