import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prometheus_node running')
@cli.command()
def start(): click.echo('prometheus_node started')
if __name__ == '__main__': cli()
