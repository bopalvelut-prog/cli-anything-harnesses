import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('segment running')
@cli.command()
def start(): click.echo('segment started')
if __name__ == '__main__': cli()
