import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('check running')
@cli.command()
def start(): click.echo('check started')
if __name__ == '__main__': cli()
