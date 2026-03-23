import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('major running')
@cli.command()
def start(): click.echo('major started')
if __name__ == '__main__': cli()
