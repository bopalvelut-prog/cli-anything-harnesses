import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('slightly running')
@cli.command()
def start(): click.echo('slightly started')
if __name__ == '__main__': cli()
