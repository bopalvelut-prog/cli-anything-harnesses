import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Chronograf running on :8888')
@cli.command()
def status(): click.echo('Chronograf status')
if __name__ == '__main__': cli()
