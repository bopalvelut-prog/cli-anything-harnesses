import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('perf running')
@cli.command()
def start(): click.echo('perf started')
if __name__ == '__main__': cli()
