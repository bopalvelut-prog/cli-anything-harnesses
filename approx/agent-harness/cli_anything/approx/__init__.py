import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('approx running')
@cli.command()
def start(): click.echo('approx started')
if __name__ == '__main__': cli()
