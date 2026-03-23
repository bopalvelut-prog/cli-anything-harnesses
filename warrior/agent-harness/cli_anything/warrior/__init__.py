import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('warrior running')
@cli.command()
def start(): click.echo('warrior started')
if __name__ == '__main__': cli()
