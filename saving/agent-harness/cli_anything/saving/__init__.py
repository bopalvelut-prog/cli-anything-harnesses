import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('saving running')
@cli.command()
def start(): click.echo('saving started')
if __name__ == '__main__': cli()
