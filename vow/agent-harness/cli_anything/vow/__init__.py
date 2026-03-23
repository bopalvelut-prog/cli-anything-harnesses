import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vow running')
@cli.command()
def start(): click.echo('vow started')
if __name__ == '__main__': cli()
