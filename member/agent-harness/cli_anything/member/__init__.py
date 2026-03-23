import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('member running')
@cli.command()
def start(): click.echo('member started')
if __name__ == '__main__': cli()
