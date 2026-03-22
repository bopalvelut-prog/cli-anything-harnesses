import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('NaiveProxy started')
@cli.command()
def status(): click.echo('NaiveProxy running')
if __name__ == '__main__': cli()
