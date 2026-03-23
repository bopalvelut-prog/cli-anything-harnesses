import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pprof running')
@cli.command()
def start(): click.echo('pprof started')
if __name__ == '__main__': cli()
