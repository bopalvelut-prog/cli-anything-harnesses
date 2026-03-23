import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hard running')
@cli.command()
def start(): click.echo('hard started')
if __name__ == '__main__': cli()
