import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dero running')
@cli.command()
def start(): click.echo('dero started')
if __name__ == '__main__': cli()
