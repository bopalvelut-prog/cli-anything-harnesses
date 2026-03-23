import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('opentsdb running')
@cli.command()
def start(): click.echo('opentsdb started')
if __name__ == '__main__': cli()
