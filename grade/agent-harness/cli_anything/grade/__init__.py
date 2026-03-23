import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grade running')
@cli.command()
def start(): click.echo('grade started')
if __name__ == '__main__': cli()
