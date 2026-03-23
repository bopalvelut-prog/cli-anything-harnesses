import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prometheus_exporter running')
@cli.command()
def start(): click.echo('prometheus_exporter started')
if __name__ == '__main__': cli()
