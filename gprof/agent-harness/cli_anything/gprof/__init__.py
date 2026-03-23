import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gprof running')
@cli.command()
def start(): click.echo('gprof started')
if __name__ == '__main__': cli()
